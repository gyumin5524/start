# 역할
# 데이터베이스 테이블을 정의하는 곳입니다.
# Django의 ORM(Object-Relational Mapping)을 사용하여 테이블과 필드 정의를 작성합니다.
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)