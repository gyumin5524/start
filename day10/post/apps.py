# 역할
# post 앱에 대한 메타데이터를 정의합니다.
# 앱의 이름을 설정하거나, 커스텀 설정을 추가할 때 사용합니다.
from django.apps import AppConfig


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
