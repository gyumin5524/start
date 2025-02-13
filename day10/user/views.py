# 역할
# 사용자 관련 HTTP 요청을 처리하고 응답을 반환하는 비즈니스 로직을 작성하는 파일입니다.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


class UserListCreateView(APIView):
    def get(self, request):
        users = User.object.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(user, id = pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        data = request.data
        user = get_object_or_404(User, id = pk)
        serializer = UserSerializer(user, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        user.delete()
        return Response({"message": "사용자가 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    def post(self, request):
        # 사용자의 id, pw 받아야해서 get
        # 처리 : 디비에서 사용자를 가져와서 확인
        # id = username / pw = password {"password" : "####"}
        username = request.data.get("username")
        password = request.data.get("password")
        # 사용자 정보가 맞는지 확인
        # authenticate : username으로 해당 유저가 있는지 확인 -> 패스워드가 맞는지 확인
        # 맞다면 -> 해당하는 user 리턴 / 틀리면 -> None
        user = authenticate(username = username, password = password)
        if user is not None:
            # 유저가 존재하고 비밀번호도 맞는 경우
            # 응답 -> 고유값 전송 get 없으면 create
            # get_or_create : 기존 토큰 확인(Token테이블에서 확인)있으면 가져오기 get / 없으면 생성 create
            token, created = Token.object.get_or_create(user = user)
            return Response({'token' : token.key}, status = status.HTTP_200_OK)
        return Response({'error' : '로그인에 실패했습니다.'}, status = status.HTTP_400_BAD_REQUEST)
    