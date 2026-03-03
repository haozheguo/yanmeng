from django.urls import path
from .views import PostListView,PostCommentListView,PostSearchView,PostTrendView,PostViewSet,PostCommentSet,PostLikeSet,CollectPostView,getCollectPostListView,getWritePostListView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('getPostlist/', PostListView.as_view(), name='post-list'),
    path('getWritePostlist/', getWritePostListView.as_view(), name='write-post-list'),
    path('collectPost/', CollectPostView.as_view(), name='collect-post'),
    path('searchPost/', PostSearchView.as_view(), name='search'),
    path('trendPost/', PostTrendView.as_view(), name='trend'),
    path('comments/<int:post_id>', PostCommentListView.as_view(), name='comment-list'),
    path('getCollectedPost/',getCollectPostListView.as_view(),name='collect-post-list'),
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register('post', PostViewSet)  # 向路由器中注册视图集
router.register('comment',PostCommentSet)
router.register('like',PostLikeSet)
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中