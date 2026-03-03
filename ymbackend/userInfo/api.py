from django.http import JsonResponse
from .models import customUser
import json
from rest_framework.decorators import api_view

@api_view(['POST'])
def loginapi(request):
    data = request.data
    print(data)
    phone = data.get('phone')
    password = data.get('password')

    user = customUser.objects.get(phone=phone)
    print(user.phone)
    if user.password == password and user.is_active == True:
        form = {
            'id': user.id,
            'name': user.name,
            'phone': user.phone,
            'ymvalue': user.ymvalue,
            'is_vip': user.is_vip,
            'avatar':user.avatar
        }
        return JsonResponse(form,safe=False)
    else:
        return JsonResponse({'error': '验证失败'}, status=400)
    