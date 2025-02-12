from django.urls import path
from .views import PostWrite, PostList, PostDetail, PostUpdate, PostDelete
from .views import PostListCreateView, PostDetailView
# 패턴 맵핑
urlpatterns = [
    path('write/', PostWrite.as_view()),            # as_view는 클래스뷰를 끌어땡겨 쓰려고 사용
    path('list/', PostList.as_view()),
    path('detail/<int:pk>/', PostDetail.as_view()), # pk라는 int형이 들어감 <str:pk>은 로컬주소뒤abc
    path('update/<int:pk>/', PostUpdate.as_view()),
    path('delete/<int:pk>/', PostDelete.as_view()),
]

# Rest API 때문에 url구성
# /post
# /post/1


urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
]