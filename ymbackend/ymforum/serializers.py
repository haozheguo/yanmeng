from rest_framework import serializers
from .models import Post,PostComment,PostLike,PostCollect
from userInfo.serializers import AuthorSerializer

class PostListSerializer(serializers.ModelSerializer):
    author =  AuthorSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'category', 'created_at', 'updated_at', 'is_delete', 'img', 'ViewNum', 'LikeNum']

class PostCommentListSerializer(serializers.ModelSerializer):
    author =  AuthorSerializer(read_only=True)
    class Meta:
        model = PostComment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at', 'is_delete']

class PostTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'category', 'created_at', 'ViewNum', 'LikeNum']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'