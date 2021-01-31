from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('add_posts/', views.add_posts, name='add_posts'),
    path('show_posts/', views.show_posts, name='show_posts'),
    path('show_posts_redis/', views.show_posts_redis, name='show_posts_redis'),
]