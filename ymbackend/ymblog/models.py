from django.db import models

from userInfo.models import customUser
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=64,verbose_name="标题")
    author = models.ForeignKey(customUser,on_delete=models.CASCADE,verbose_name="作者")
    abstract = models.TextField(verbose_name="摘要")
    category=models.CharField(max_length=32,verbose_name="分类")
    tag1 = models.CharField(max_length=32,verbose_name="标签1",blank=True,default="考研")
    tag2 = models.CharField(max_length=32,verbose_name="标签2",blank=True,default="顺利")
    tag3 = models.CharField(max_length=32,verbose_name="标签3",blank=True,default="上岸")
    ViewNum = models.IntegerField(default=0,verbose_name="浏览量")
    LikeNum = models.IntegerField(default=0,verbose_name="点赞量")
    content = models.TextField(verbose_name="内容")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    is_delete = models.BooleanField(default=False,verbose_name="删除状态")
    is_vip = models.BooleanField(default=False,verbose_name="VIP专属")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "文章"

class Comment(models.Model):
    user = models.ForeignKey(customUser,on_delete=models.CASCADE,verbose_name="用户")
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="文章")
    content = models.TextField(verbose_name="评论内容")
    comment_time = models.DateTimeField(auto_now_add=True,verbose_name="评论时间")
    is_delete = models.BooleanField(default=False,verbose_name="删除状态")

    def __str__(self):
        return self.user.username + "评论了" + self.article.title
    
    class Meta:
        verbose_name = "文章评论"

class LikeArticle(models.Model):
    user = models.ForeignKey(customUser,on_delete=models.CASCADE,verbose_name="用户")
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="文章")
    like_time = models.DateTimeField(auto_now_add=True,verbose_name="点赞时间")

    def __str__(self):
        return self.user.username + "点赞了" + self.article.title
    
    class Meta:
        verbose_name = "点赞记录"

class CollectArticle(models.Model):
    user = models.ForeignKey(customUser,on_delete=models.CASCADE,verbose_name="用户")
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="文章")
    collect_time = models.DateTimeField(auto_now_add=True,verbose_name="收藏时间")

    def __str__(self):
        return self.user.username + "收藏了" + self.article.title
    
    class Meta:
        verbose_name = "收藏记录"

# class SpiderArticle(models.Model):
#     title = models.CharField(max_length=64,verbose_name="标题")
#     category=models.CharField(max_length=32,verbose_name="分类")
#     content = models.TextField(verbose_name="内容")
#     create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
#     link = models.CharField(max_length=255, blank=True)
     
#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = "爬虫文章"