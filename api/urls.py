from django.urls import path

from .views import PostListAPIView, PostDetailAPIView, CommentCreateAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='api-posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='api-post-detail'),
    path('posts/<int:post_id>/comments/', CommentCreateAPIView.as_view(), name='api-comments'),
]
