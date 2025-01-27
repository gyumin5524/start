# 역할
# 데이터베이스 테이블을 정의하는 파일입니다.
# 사용자와 관련된 데이터 구조를 설계합니다.
# 기본 사용자 모델(AbstractUser 또는 AbstractBaseUser)을 커스터마이징하여 확장할 때 사용됩니다.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()