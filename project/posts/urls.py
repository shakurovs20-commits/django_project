from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('groups/all/', views.groups, name='all_groups'),
    # path('post/new/',
    #      views.post_create, name='post_create'),
    path('post/new/',
         views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('my/profile/', views.profile, name='my_profile'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('<str:username>/follow/', views.profile_follow, name='follow'),
    path('<str:username>/unfollow/', views.profile_unfollow, name='unfollow'),
    path('my/following', views.follow_index, name='follow_index'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
]