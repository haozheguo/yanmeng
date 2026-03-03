from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import scrapyArticleViewSet,scrapyArticleStatsAPIView,scrapyArticleKeywordsView
# 路由列表
urlpatterns = [
     path('getScrapylist/', scrapyArticleStatsAPIView.as_view(), name='article-list'),
     path('getScrapyKeywords/',scrapyArticleKeywordsView.as_view(),name='scrapy-keywords-list')
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register('scrapy', scrapyArticleViewSet)  # 向路由器中注册视图集
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中