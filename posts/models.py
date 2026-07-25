from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts/')
    caption = models.CharField(max_length=255, blank=True)

    # Nutrition info (Flex Calories)
    food_name = models.CharField(max_length=150, blank=True)
    calories = models.FloatField(default=0)
    protein = models.FloatField(default=0)   # grams
    carbs = models.FloatField(default=0)     # grams
    fat = models.FloatField(default=0)       # grams

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # naye posts sabse upar

    def __str__(self):
        return f"{self.user.username} - {self.food_name or 'Post'}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # ek user ek post ko ek hi baar like kare

    def __str__(self):
        return f"{self.user.username} liked {self.post}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user.username}: {self.text[:30]}"
