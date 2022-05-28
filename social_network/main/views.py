from django.shortcuts import render
from django.forms import ValidationError
from rest_framework import generics
from .models import Post, LikeDislike
from .serializers import PostSerializer, CreateLikeSerializer, CreatePostSerializer


class NewPostCreateAPIView(generics.CreateAPIView):
    """Add new post"""
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer


class GetPostListView(generics.ListAPIView):
    """Show all posts"""
    queryset = Post.objects.prefetch_related('likes')
    serializer_class = PostSerializer


class NewLikeDislikeCreateAPIView(generics.CreateAPIView):
    """Add like or dislike"""
    queryset = LikeDislike.objects.all()
    serializer_class = CreateLikeSerializer

    def perform_create(self, serializer):
        user = serializer.validated_data.get('user')
        if LikeDislike.objects.filter(
            user=user
        ).exists():
            raise ValidationError(
                'You left a like/dislike before.')
        else:
            serializer.save(user=user)
