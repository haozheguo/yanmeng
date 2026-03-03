from django.urls import path
from .views import ArticleListView,ArticleViewSet,CommentViewSet,LikeArticleViewSet,CommentListView,ArticleSearchView,ArticleTrendView,CollectArticleView,getCollectArticleListView,ArticleKeyWordView,getWriteArticleListView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('getArticlelist/', ArticleListView.as_view(), name='article-list'),
    path('getCollectArticlelist/', getCollectArticleListView.as_view(), name='collect-article-list'),
    path('getWriteArticlelist/', getWriteArticleListView.as_view(), name='write-article-list'),
    path('collectArticle/', CollectArticleView.as_view(), name='collect-article'),
    path('comments/<int:article_id>', CommentListView.as_view(), name='comment-list'),
    path('searchArticle/', ArticleSearchView.as_view(), name='article-search'),
    path('trendArticle/', ArticleTrendView.as_view(), name='article-trend'),
    path('articleKeywords/<int:article_id>',ArticleKeyWordView.as_view(),name='article-keywords'),
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register('article', ArticleViewSet)  # 向路由器中注册视图集
router.register('commentarticle', CommentViewSet)
router.register('likearticle', LikeArticleViewSet)
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中