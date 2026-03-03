from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import scrapyArticle
from .serializers import scrapyArticleSerializer,scrapyArticleStatsSerializer
import jieba.analyse
import re
# Create your views here.
class scrapyArticleViewSet(viewsets.ModelViewSet):
    queryset = scrapyArticle.objects.all()
    serializer_class = scrapyArticleSerializer
    
class scrapyArticleStatsAPIView(APIView):
    def get(self, request):
        # 获取所有文章
        queryset = scrapyArticle.objects.all()

        # 构建返回的数据结构
        data = {
            'allNum': queryset.count(),
            'yanzhaoNum': queryset.filter(category='研招网').count(),
            'wechatNum': queryset.filter(category='微信').count(),
            'baiduNum': queryset.filter(category='百度').count(),
            'positiveNum': queryset.filter(emotion='积极').count(),
            'normalNum': queryset.filter(emotion='中性').count(),
            'negativeNum': queryset.filter(emotion='消极').count(),
            'yanzhaoList': [],
            'wechatList': [],
            'baiduList': [],
        }

        # 获取前五条数据
        yanzhao_articles = queryset.filter(category='研招网').order_by('-created_time')[:5]
        wechat_articles = queryset.filter(category='微信').order_by('-created_time')[:5]
        baidu_articles = queryset.filter(category='百度').order_by('-created_time')[:5]

        # 构建前五条数据的列表
        for article in yanzhao_articles:
            data['yanzhaoList'].append({
                'title': article.title,
                'category': article.category,
                'emotion': article.emotion,
                'created_time': article.created_time,
                'url': article.url
            })

        for article in wechat_articles:
            data['wechatList'].append({
                'title': article.title,
                'category': article.category,
                'emotion': article.emotion,
                'created_time': article.created_time,
                'url': article.url
            })

        for article in baidu_articles:
            data['baiduList'].append({
                'title': article.title,
                'category': article.category,
                'emotion': article.emotion,
                'created_time': article.created_time,
                'url': article.url
            })

        # 返回封装的 JSON 数据
        return Response(data)
    
# 获取按时间排序的文章内容并提取关键词
class scrapyArticleKeywordsView(APIView):
    def get(self,request):
        queryset = scrapyArticle.objects.all().order_by('-created_time')[:5]
        # 获取5篇文章的内容字段
        contents = queryset.values_list('content', flat=True)
        combined_content = ' '.join(contents)
         # 去掉文本中的markdown格式符号
        combined_content_cleaned = re.sub(r'(?<!\\)[*_]{1,3}|^(#+\s+)', '', combined_content, flags=re.MULTILINE)
        # 使用jieba进行关键词提取
        keywords = jieba.analyse.extract_tags(combined_content_cleaned, topK=15, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
         # 将提取到的关键词转换为所需的格式
        wordCloudData = [{'name': keyword, 'value': 10} for keyword, weight in keywords]
        
        # 返回关键词数据
        return Response(wordCloudData)

# 返回对某篇文章的TD-IDF关键词分析数据
# class ArticleKeyWordView(APIView):
#     def get(self, request, article_id):
#         article = Article.objects.get(id=article_id)
#         # 获取文章的内容
#         content = article.content
#         # 去掉content中包含的markdown格式的一些符号
#         import re
#         content_cleaned = re.sub(r'(?<!\\)[*_]{1,3}|^(#+\s+)', '', content, flags=re.MULTILINE)
#         # 使用jieba分词
#         import jieba.analyse
#         # 获取文章的关键词
#         keywords = jieba.analyse.extract_tags(content_cleaned, topK=15, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
#         # 将keywords包装成wordCloudData: [
#             #     { name: '考研', value: 100 },
#             #     { name: '经验分享', value: 80 },
#             # ]格式
#         wordCloudData = [{'name': keyword, 'value': weight} for keyword, weight in keywords]
#         return Response(wordCloudData)
