
from django.urls import path
from .views import ElonlarListAPIView,CategoryElonlarListAPIView,CategoryYangiliklarListAPIView,YangiliklarListAPIView,CategoryYangiliklarCreateAPIView, CategoryElonlarCreateAPIView,YangiliklarCreateAPIView,ElonlarCreateAPIView

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Geologiya API')



urlpatterns = [
    url(r'^$', schema_view),
    path("elonlar/",ElonlarListAPIView.as_view()),
    path("elonlar/category/",CategoryElonlarListAPIView.as_view()),
    path("yangiliklar/category/",CategoryYangiliklarListAPIView.as_view()),
    path("yangiliklar/",YangiliklarListAPIView.as_view()),
    path("yangiliklar/category/<int:pk>/",CategoryYangiliklarCreateAPIView.as_view()),
    path("elonlar/category/<int:pk>/",CategoryElonlarCreateAPIView.as_view()),
    path("yangiliklar/<int:pk>/",YangiliklarCreateAPIView.as_view()),
    path("elonlar/<int:pk>/",ElonlarCreateAPIView.as_view()),

]
