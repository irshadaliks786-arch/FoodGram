from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption', 'food_name', 'calories', 'protein', 'carbs', 'fat']
        widgets = {
            'caption': forms.TextInput(attrs={'placeholder': 'Caption likho...'}),
            'food_name': forms.TextInput(attrs={'placeholder': 'Jaise: Chicken Biryani'}),
        }
