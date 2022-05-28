from rest_framework import serializers
from .models import Post, LikeDislike


class CreateLikeSerializer(serializers.ModelSerializer):
    """Add like or dislike"""
    class Meta:
        model = LikeDislike
        fields = "__all__"


class CreatePostSerializer(serializers.ModelSerializer):
    """Add new post"""
    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    """Like serializer"""
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    post = serializers.SlugRelatedField(
        slug_field='title', read_only=True)

    class Meta:
        model = LikeDislike
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """Post serializer"""
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    likes = LikeSerializer(many=True)
    count_all_likes = serializers.SerializerMethodField()
    count_likes = serializers.SerializerMethodField()
    count_dislikes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_count_all_likes(self, obj):
        return obj.likes.count()

    def get_count_likes(self, obj):
        return LikeDislike.objects.filter(post=obj).filter(like='like').count()

    def get_count_dislikes(self, obj):
        return LikeDislike.objects.filter(post=obj).filter(like='dislike').count()
