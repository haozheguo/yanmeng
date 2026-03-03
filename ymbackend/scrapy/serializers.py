from rest_framework import serializers
from .models import scrapyArticle

class scrapyArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = scrapyArticle
        fields = '__all__'

from rest_framework import serializers
from .models import scrapyArticle

class scrapyArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = scrapyArticle
        fields = '__all__'

class scrapyArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = scrapyArticle
        fields = ['title','category','emotion','created_time','url']

    
class scrapyArticleStatsSerializer(serializers.Serializer):
    allNum = serializers.IntegerField()
    yanzhaoNum = serializers.IntegerField()
    wechatNum = serializers.IntegerField()
    baiduNum = serializers.IntegerField()
    positiveNum = serializers.IntegerField()
    normalNum = serializers.IntegerField()
    negativeNum = serializers.IntegerField()
    yanzhaoList = serializers.ListField(child=serializers.DictField())
    wechatList = serializers.ListField(child=serializers.DictField())
    baiduList = serializers.ListField(child=serializers.DictField())

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # 计算总数
        representation['allNum'] = instance.count()

        # 计算各分类数目
        representation['yanzhaoNum'] = instance.filter(category='研招网').count()
        representation['wechatNum'] = instance.filter(category='微信').count()
        representation['baiduNum'] = instance.filter(category='百度').count()

        # 计算情感数目
        representation['positiveNum'] = instance.filter(emotion='积极').count()
        representation['normalNum'] = instance.filter(emotion='中性').count()
        representation['negativeNum'] = instance.filter(emotion='消极').count()

        # 获取前五条数据
        yanzhao_articles = instance.filter(category='研招网').order_by('-created_time')[:5]
        wechat_articles = instance.filter(category='微信').order_by('-created_time')[:5]
        baidu_articles = instance.filter(category='百度').order_by('-created_time')[:5]

        # 序列化前五条数据
        yanzhao_serializer = scrapyArticleListSerializer(yanzhao_articles, many=True)
        wechat_serializer = scrapyArticleListSerializer(wechat_articles, many=True)
        baidu_serializer = scrapyArticleListSerializer(baidu_articles, many=True)

        representation['yanzhaoList'] = yanzhao_serializer.data
        representation['wechatList'] = wechat_serializer.data
        representation['baiduList'] = baidu_serializer.data

        return representation
