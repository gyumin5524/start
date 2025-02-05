# 역할
# HTTP 요청을 처리하고, 적절한 응답(HTML, JSON 등)을 반환합니다.
# 비즈니스 로직을 구현하는 곳입니다.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        #응답: 직렬화(serializer), 데이터베이스에서 가져온 데이터 raw데이터 -> json데이터
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PostWrite(APIView):
    def post(self, request):
        #응답 역직렬화, json데이터 -> raw데이터 
        serializer = PostSerializer(data = request.data) # data = 들어가면 역직렬화
        #사용자에게 받은 값은 유효성 검증이 필수(악성데이터인지 아닌지)
        if serializer.is_valid():
            serializer.save() #True, 저장
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# Create your views here.
