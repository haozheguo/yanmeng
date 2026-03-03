from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Article, Comment, LikeArticle, CollectArticle
from .serializers import ArticleListSerializer, ArticleSerializer, ArticleTrendSerializer,CommentSerializer,  LikeArticleSerializer, CollectArticleSerializer,CommentListSerializer
from rest_framework import viewsets
from django.utils import timezone

# 获取分类的文章列表
class ArticleListView(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        
        if category:
            queryset = Article.objects.filter(category=category, is_delete=False).order_by('-create_time')
        else:
            queryset = Article.objects.filter(is_delete=False).order_by('-create_time')
        
        serializer = ArticleListSerializer(queryset, many=True)
        return Response(serializer.data)

# 获取某一用户收藏的文章列表
class getCollectArticleListView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        # 获取该用户所有的收藏文章
        collect_articles = CollectArticle.objects.filter(user=user_id).order_by('-collect_time')
        # 获取所有收藏文章的ID
        article_ids = collect_articles.values_list('article', flat=True)
        # 根据文章ID查询文章
        articles = Article.objects.filter(id__in=article_ids,is_delete=False)
        # 使用ArticleListSerializer对文章列表数据进行序列化
        serializer = ArticleListSerializer(articles, many=True)
        # 返回序列化后的数据
        return Response(serializer.data)

# 获得某一用户发布的文章列表
class getWriteArticleListView(APIView):
    def get(self,request):
        user_id = request.query_params.get('user_id')
        # 获取该用户发布的所有文章
        myArticles = Article.objects.filter(author=user_id,is_delete=False).order_by('-create_time')
        # 使用ArticleListSerializer对文章列表数据进行序列化
        serializer = ArticleListSerializer(myArticles, many=True)
        # 返回序列化后的数据
        return Response(serializer.data)
    
# 收藏文章
class CollectArticleView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        article_id = request.query_params.get('article_id')
        try:
            collect_article = CollectArticle.objects.get(user=user_id, article=article_id)
            # 更新收藏时间
            collect_article.collect_time = timezone.now()
            collect_article.save()
            # 返回 type: false
            return Response({'type': False})
        except CollectArticle.DoesNotExist:
            # 创建新的收藏记录
            collect_article = CollectArticle.objects.create(user_id=user_id, article_id=article_id)
            # 返回 type: true
            return Response({'type': True})

# 根据参数搜索文章
class ArticleSearchView(APIView):
    def get(self,request):
        search = request.query_params.get('search')
        articles = Article.objects.filter(is_delete=False)  # 先过滤掉被删除的文章

        if search:
            articles = articles.filter(
                Q(title__icontains=search) | Q(abstract__icontains=search)
            ).order_by('-create_time')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

# 获取文章的趋势
class ArticleTrendView(APIView):
    def get(self,request):
        queryset = Article.objects.filter(is_delete=False).order_by('-ViewNum')[:5]
        serializer = ArticleTrendSerializer(queryset, many=True)
        return Response(serializer.data)
        

# 获取某篇文章下的评论列表
class CommentListView(APIView):
    def get(self, request, article_id):
        # 从数据库中获取对应文章下的评论
        comments = Comment.objects.filter(article=article_id, is_delete=False)
        
        # 序列化评论列表
        serializer = CommentListSerializer(comments, many=True)
        
        return Response(serializer.data)

# 返回对某篇文章的TD-IDF关键词分析数据
class ArticleKeyWordView(APIView):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        # 获取文章的内容
        content = article.content
        # 去掉content中包含的markdown格式的一些符号
        import re
        content_cleaned = re.sub(r'(?<!\\)[*_]{1,3}|^(#+\s+)', '', content, flags=re.MULTILINE)
        # 使用jieba分词
        import jieba.analyse
        # 获取文章的关键词
        keywords = jieba.analyse.extract_tags(content_cleaned, topK=15, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
        # 将keywords包装成wordCloudData: [
            #     { name: '考研', value: 100 },
            #     { name: '经验分享', value: 80 },
            # ]格式
        wordCloudData = [{'name': keyword, 'value': 10} for keyword, weight in keywords]
        return Response(wordCloudData)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeArticleViewSet(viewsets.ModelViewSet):
    queryset = LikeArticle.objects.all()
    serializer_class = LikeArticleSerializer