from rest_framework import serializers
from .models import CategoryElonlar,Elonlar,CategoryYangiliklar,Yangiliklar

class CategoryElonlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryElonlar
        fields = ['title']

class CategoryYangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryYangiliklar
        fields = ['title']


class ElonlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elonlar
        fields = ['category','title','content','created_at','updated_at']



class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ['category','title','content','created_at','updated_at']