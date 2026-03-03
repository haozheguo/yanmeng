from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import Post, PostComment, PostLike, PostCollect,customUser
from .serializers import PostListSerializer, PostSerializer,PostCommentSerializer,PostCommentListSerializer,PostLikeSerializer,PostTrendSerializer
from django.utils import timezone

# 获取帖子列表
class PostListView(APIView):
    def get(self,request):
        category = request.query_params.get('category')
        id = request.query_params.get('id')
        if category:
            queryset = Post.objects.filter(category=category,is_delete=False).order_by('-created_at')
        elif id:
            try:
                post = Post.objects.get(id=id, is_delete=False)
                serializer = PostListSerializer(post)
                return Response(serializer.data)
            except Post.DoesNotExist:
                return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Post.objects.filter(
                is_delete=False).order_by('-created_at')[:20]
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)

# 获取文章收藏列表
class CollectPostView(APIView):
    def get(self, request):
        author_id = request.query_params.get('author_id')
        post_id = request.query_params.get('post_id')
        try:
            author = customUser.objects.get(id=author_id)
            post = Post.objects.get(id=post_id)
            collectPost = PostCollect.objects.get(author=author, post=post)
            # 更新收藏时间
            collectPost.created_at = timezone.now()
            collectPost.save()
            # 返回 type: false
            return Response({'type': False})
        except PostCollect.DoesNotExist:
            # 创建新的收藏记录
            collectPost = PostCollect.objects.create(author=author, post=post)
            # 返回 type: true
            return Response({'type': True})

# 返回帖子搜索结果
class PostSearchView(APIView):
    def get(self,request):
        search = request.query_params.get('search')
        queryset = Post.objects.filter(content__contains=search,is_delete=False).order_by('-created_at')
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)

# 获取热门帖子列表
class PostTrendView(APIView):
    def get(self,request):
        queryset = Post.objects.filter(is_delete=False).order_by('-ViewNum')[:5]
        serializer = PostTrendSerializer(queryset, many=True)
        return Response(serializer.data)
        
# 获取帖子评论列表
class PostCommentListView(APIView):
    def get(self, request, post_id):
        # 从数据库中获取对应文章下的评论
        comments = PostComment.objects.filter(post=post_id, is_delete=False)
        
        # 序列化评论列表
        serializer = PostCommentListSerializer(comments, many=True)
        
        return Response(serializer.data)

# 获取某一用户发布的帖子列表
class getWritePostListView(APIView):
    def get(self,request):
        author_id = request.query_params.get('author_id')
        # 获取该用户发布的所有帖子
        myPosts = Post.objects.filter(author=author_id,is_delete=False).order_by('-created_at')
        # 使用PostListSerializer对帖子列表数据进行序列化
        serializer = PostListSerializer(myPosts, many=True)
        return Response(serializer.data)

# 获取某一用户收藏的帖子列表
class getCollectPostListView(APIView):
    def get(self,request):
        author_id = request.query_params.get('author_id')
        # 获取该用户所有的收藏帖子
        collect_posts = PostCollect.objects.filter(author=author_id).order_by('-created_at')
        # 获得所有收藏帖子的id
        post_ids = collect_posts.values_list('post', flat=True)
        # 根据帖子id查找帖子
        posts = Post.objects.filter(id__in=post_ids,is_delete=False)
        # 使用PostListSerializer对帖子列表数据进行序列化
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)       

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCommentSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

class PostLikeSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer