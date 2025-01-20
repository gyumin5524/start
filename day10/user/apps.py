# 역할
# user 앱의 설정 정보를 정의합니다.
# Django 프로젝트가 앱을 식별하고 관리할 수 있도록 합니다.
from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
