from django.db import models
from userInfo.models import customUser
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(customUser,on_delete=models.CASCADE,verbose_name="作者")
    content = models.TextField(verbose_name="内容")
    category=models.CharField(max_length=32,verbose_name="分类")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="发布时间")
    is_delete = models.BooleanField(default=False,verbose_name="删除状态")
    img = models.CharField(max_length=255, blank=True, verbose_name="图片链接")
    ViewNum = models.IntegerField(default=0,verbose_name="浏览量")
    LikeNum = models.IntegerField(default=0,verbose_name="点赞量")
    
    class Meta:
        verbose_name = "帖子"
    
class PostComment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="帖子")
    author = models.ForeignKey(customUser,on_delete=models.CASCADE,verbose_name="评论者")
    content = models.TextField(verbose_name="内容")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="发布时间")
    is_delete = models.BooleanField(default=False,verbose_name="删除状态")
    
    class Meta:
        verbose_name = "帖子评论"

class PostLike(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="帖子")
    author = models.ForeignKey(customUser,on_delete=models.CASCADE,verbose_name="作者")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    
    class Meta:
        verbose_name = "帖子点赞"

class PostCollect(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="帖子")
    author = models.ForeignKey(customUser,on_delete=models.CASCADE,verbose_name="作者")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    
    class Meta:
        verbose_name = "帖子收藏"
