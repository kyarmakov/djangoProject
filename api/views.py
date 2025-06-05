from rest_framework import generics

from blog.models import Post
from .serializers import PostSerializer, CommentSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
