from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.conf import settings
import os
import uuid
from .models import customUser
from .serializers import CustomUserSerializer,AuthorSerializer

class UserViewSet(ModelViewSet):
    queryset = customUser.objects.all()
    serializer_class = CustomUserSerializer
    
class AuthorViewSet(ModelViewSet):
    queryset = customUser.objects.all()
    serializer_class = AuthorSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_media(request):
    file_obj = request.FILES.get('file')
    folder = request.data.get('folder', 'uploads')
    if file_obj is None:
        return Response({'error': 'file is required'}, status=400)

    if folder not in {'post', 'avator', 'uploads'}:
        folder = 'uploads'

    ext = os.path.splitext(file_obj.name)[1].lower()
    filename = f"{uuid.uuid4().hex}{ext}"
    relative_path = default_storage.save(f"{folder}/{filename}", file_obj)
    media_url = settings.MEDIA_URL + relative_path
    absolute_url = request.build_absolute_uri(media_url)
    return Response({'url': absolute_url, 'path': media_url})
