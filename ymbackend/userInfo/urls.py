from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api import loginapi
# 路由列表
urlpatterns = [
    # 配置api文档路由 title配置API文档的标题
    
    path('login/', loginapi, name='login'),
    path('upload/', views.upload_media, name='upload-media'),
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register('users', views.UserViewSet)  # 向路由器中注册视图集
router.register('author',views.AuthorViewSet)
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
