from rest_framework import serializers
from .models import customUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = '__all__'
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ['name','avatar','ymvalue','is_vip']

# class customUser(models.Model):
#     name = models.CharField(max_length=64,blank=True,default='用户',verbose_name="用户名")
#     phone = models.CharField(max_length=13,unique=True,verbose_name="电话")
#     password = models.CharField(max_length=64,verbose_name="密码")
#     is_active = models.BooleanField(default=True,blank=True,verbose_name="激活状态")
#     is_vip = models.BooleanField(default=False,blank=True,verbose_name="是否是VIP")
#     ymvalue = models.IntegerField(default=0,verbose_name="研梦值")
#     create_at = models.DateTimeField(default=timezone.now,verbose_name="创建时间")
#     avatar = models.CharField(max_length=255, blank=True, default='http://127.0.0.1:8000/media/avator/defaultavator.png', verbose_name="头像")
    
    

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = "研梦用户"