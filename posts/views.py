from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import JsonResponse
import requests
from .models import Post, Like, Comment
from .forms import PostForm


@login_required
def feed(request):
    """Sabhi logon ke posts, sabse naya sabse upar"""
    posts = Post.objects.select_related('user').prefetch_related('likes', 'comments')
    liked_post_ids = Like.objects.filter(user=request.user).values_list('post_id', flat=True)
    return render(request, 'posts/feed.html', {
        'posts': posts,
        'liked_post_ids': set(liked_post_ids),
    })


@login_required
def upload_post(request):
    """Naya post (photo + nutrition) upload karne ke liye"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'posts/upload.html', {'form': form})


@login_required
def toggle_like(request, post_id):
    """Like/Unlike ek hi button se toggle hota hai"""
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  # already liked tha, toh unlike kar do
    return redirect('feed')


@login_required
def add_comment(request, post_id):
    """Post pe comment add karne ke liye"""
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            Comment.objects.create(user=request.user, post=post, text=text)
    return redirect('feed')


@login_required
def profile(request, username=None):
    """User ka profile — total posts aur total calories flexed"""
    user = get_object_or_404(User, username=username) if username else request.user
    posts = Post.objects.filter(user=user)
    total_calories = posts.aggregate(total=Sum('calories'))['total'] or 0
    return render(request, 'posts/profile.html', {
        'profile_user': user,
        'posts': posts,
        'total_posts': posts.count(),
        'total_calories': total_calories,
    })


@login_required
def fetch_nutrition(request):
    """
    Open Food Facts se food name ke basis pe nutrition data laata hai.
    Frontend se GET request aati hai: /nutrition-search/?food_name=chicken biryani
    Response: {"success": true, "calories": .., "protein": .., "carbs": .., "fat": ..}
    """
    food_name = request.GET.get('food_name', '').strip()
    if not food_name:
        return JsonResponse({'success': False, 'error': 'Food name khali hai'})

    url = 'https://world.openfoodfacts.org/cgi/search.pl'
    params = {
        'search_terms': food_name,
        'search_simple': 1,
        'action': 'process',
        'json': 1,
        'page_size': 5,  # top 5 results mein se pehla usable product dhoondhenge
    }
    # Open Food Facts bina User-Agent ke requests block/reject kar sakta hai
    headers = {
        'User-Agent': 'FoodGram/1.0 (Django learning project)'
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        products = data.get('products', [])

        # Kuch products mein nutriments missing hote hain, isliye pehla valid product dhoondho
        for product in products:
            nutriments = product.get('nutriments', {})
            calories = nutriments.get('energy-kcal_100g')
            if calories is not None:
                return JsonResponse({
                    'success': True,
                    'product_name': product.get('product_name', food_name),
                    'calories': round(calories, 1),
                    'protein': round(nutriments.get('proteins_100g', 0), 1),
                    'carbs': round(nutriments.get('carbohydrates_100g', 0), 1),
                    'fat': round(nutriments.get('fat_100g', 0), 1),
                    'note': 'Values per 100g — apni serving size ke hisaab se adjust kar le',
                })

        return JsonResponse({'success': False, 'error': 'Nutrition data nahi mila iske liye. Manually daal de.'})

    except requests.RequestException as e:
        # Terminal mein exact error print hoga taaki debug karna easy ho
        print(f"[fetch_nutrition] API error: {e}")
        return JsonResponse({'success': False, 'error': f'API se connect nahi ho paaya ({type(e).__name__}). Manually daal de.'})