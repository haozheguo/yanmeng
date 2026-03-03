from rest_framework import serializers
from .models import Article,Comment,LikeArticle,CollectArticle
from userInfo.serializers import AuthorSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'author_name', 'abstract', 'category', 'tag1', 'tag2', 'tag3', 'ViewNum', 'LikeNum', 'content', 'create_time', 'is_delete', 'is_vip']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
class ArticleTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'category', 'ViewNum', 'LikeNum', 'is_delete', 'is_vip']

class CommentListSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'article', 'user', 'content', 'comment_time', 'is_delete']
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeArticle
        fields = '__all__'

class CollectArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectArticle
        fields = '__all__'

