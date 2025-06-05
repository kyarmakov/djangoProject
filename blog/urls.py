from django.urls import path

from .views import PostsListView, PostDetailView, AddCommentView, PostCreateView

urlpatterns = [
    path('', PostsListView.as_view(), name='post-list'),
    path('create-post/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/add_comment/', AddCommentView.as_view(), name='add-comment'),
]
