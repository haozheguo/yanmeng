from django.contrib import admin

# Register your models here.
admin.site.site_header = '研梦后台管理系统'
admin.site.site_title = '研梦后台管理系统'
admin.site.index_title = '研梦后台管理系统'

from .models import customUser

class customUserAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','is_active','is_vip','ymvalue','create_at','avatar')
    readonly_fields = ['id', 'name','phone','avatar']  # 定义只读字段为 id 和 create_at
    exclude = ['password']  # 排除密码字段
    search_fields = ['name','phone']
    def has_add_permission(self, request):
        return False  # 阻止新增

    def has_delete_permission(self, request, obj=None):
        return False  # 阻止删除

admin.site.register(customUser,customUserAdmin)