from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('upload/', views.upload_post, name='upload_post'),
    path('nutrition-search/', views.fetch_nutrition, name='fetch_nutrition'),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('profile/', views.profile, name='my_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
