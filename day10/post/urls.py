from django.urls import path
from .views import PostWrite, PostList, PostDetail

# 패턴 맵핑
urlpatterns = [
    path('write/', PostWrite.as_view()),
    path('list/', PostList.as_view()),
    path('detail/<int:pk>/', PostDetail.as_view()), # pk라는 int형이 들어감 <str:pk>은 로컬주소뒤abc
]