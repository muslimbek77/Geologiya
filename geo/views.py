from django.shortcuts import render

from rest_framework import generics

from .models import CategoryYangiliklar,CategoryElonlar,Elonlar,Yangiliklar
from .serializers import CategoryElonlarSerializer,CategoryYangiliklarSerializer,YangiliklarSerializer,ElonlarSerializer

#cread
class CategoryElonlarCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryElonlarSerializer
    queryset = CategoryElonlar.objects.all()


class YangiliklarCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = YangiliklarSerializer
    queryset = Yangiliklar.objects.all()

class ElonlarCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ElonlarSerializer
    queryset = Elonlar.objects.all()


class CategoryYangiliklarCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryYangiliklarSerializer
    queryset = CategoryYangiliklar.objects.all()


#read
class CategoryYangiliklarListAPIView(generics.ListAPIView):
    model = CategoryYangiliklar
    serializer_class = CategoryYangiliklarSerializer
    queryset = CategoryYangiliklar.objects.all()

class CategoryElonlarListAPIView(generics.ListAPIView):
    model = CategoryElonlar
    serializer_class = CategoryElonlarSerializer
    queryset = CategoryElonlar.objects.all()

class YangiliklarListAPIView(generics.ListAPIView):
    model = Yangiliklar
    serializer_class = YangiliklarSerializer
    queryset = Yangiliklar.objects.all()

class ElonlarListAPIView(generics.ListAPIView):
    model = Elonlar
    serializer_class = ElonlarSerializer
    queryset = Elonlar.objects.all()

