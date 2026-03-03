from django.contrib import admin

from .models import Post, PostComment, PostLike, PostCollect
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','author','content','category','created_at','updated_at','is_delete',)
    readonly_fields = ['id','author','content','img','created_at','updated_at','ViewNum','LikeNum']
    search_fields = ['content','author__name']  # 允许搜索内容
    def has_add_permission(self, request):
        return False  # 阻止新增

    def has_delete_permission(self, request, obj=None):
        return False  # 阻止删除

admin.site.register(Post,PostAdmin)

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('id','post','author','content','created_at','updated_at','is_delete',)
    readonly_fields = ['id','post','author','content','created_at','updated_at']
    search_fields = ['content','author__name']  # 允许搜索评论内容
    def has_add_permission(self, request):
        return False  # 阻止新增

    def has_delete_permission(self, request, obj=None):
        return False  # 阻止删除

admin.site.register(PostComment,PostCommentAdmin)

class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id','post','author','created_at',)
    readonly_fields = ['id','post','author','created_at']
    search_fields = ['author__name', 'post__content']
    def has_add_permission(self, request):
        return False  # 阻止新增

    def has_delete_permission(self, request, obj=None):
        return False  # 阻止删除
admin.site.register(PostLike,PostLikeAdmin)

class PostCollectAdmin(admin.ModelAdmin):
    list_display = ('id','post','author','created_at',)
    readonly_fields = ['id','post','author','created_at']
    search_fields = ['author__name', 'post__content']
    def has_add_permission(self, request):
        return False  # 阻止新增

    def has_delete_permission(self, request, obj=None):
        return False  # 阻止删除

admin.site.register(PostCollect,PostCollectAdmin)