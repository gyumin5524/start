from django.urls import path
from .views import PostWrite, PostList

urlpatterns = [
    path('write/', PostWrite.as_view()),
    path('list/', PostList.as_view())
]