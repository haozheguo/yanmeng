from django.contrib import admin

# Register your models here.
from .models import Article,Comment,LikeArticle,CollectArticle

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','abstract','author','category','create_time','update_time','is_delete','is_vip',)
    readonly_fields = ['id','title','abstract','author','content','create_time','update_time','ViewNum','LikeNum']
    search_fields = ['title', 'abstract']  # 允许搜索标题和摘要
    def has_add_permission(self, request):
        return False  # 阻止新增

    def has_delete_permission(self, request, obj=None):
        return False  # 阻止删除

admin.site.register(Article,ArticleAdmin)

class CommentArticleAdmin(admin.ModelAdmin):
    list_display = ('id','user','article','content','comment_time','is_delete',)
    readonly_fields = ['id','user','article','content','comment_time']
    search_fields = ['content','user__name']  # 允许搜索评论内容
    def has_add_permission(self, request):
        return False  # 阻止新增

    def has_delete_permission(self, request, obj=None):
        return False  # 阻止删除

admin.site.register(Comment,CommentArticleAdmin)

class LikeArticleAdmin(admin.ModelAdmin):
    list_display = ('id','user','article','like_time',)
    readonly_fields = ['id','user','article','like_time']
    search_fields = ['user__name', 'article__title'] 
    def has_add_permission(self, request):
        return False  # 阻止新增

    def has_delete_permission(self, request, obj=None):
        return False  # 阻止删除

admin.site.register(LikeArticle,LikeArticleAdmin)

class CollectedArticleAdmin(admin.ModelAdmin):
    list_display = ('id','user','article','collect_time',)
    readonly_fields = ['id','user','article','collect_time']
    search_fields = ['user__name', 'article__title']
    def has_add_permission(self, request):
        return False  # 阻止新增

    def has_delete_permission(self, request, obj=None):
        return False  # 阻止删除

admin.site.register(CollectArticle,CollectedArticleAdmin)