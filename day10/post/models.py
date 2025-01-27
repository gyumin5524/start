# 역할
# 데이터베이스 테이블을 정의하는 곳입니다.
# Django의 ORM(Object-Relational Mapping)을 사용하여 테이블과 필드 정의를 작성합니다.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500, null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

