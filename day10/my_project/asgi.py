# 역할
# Django 프로젝트가 비동기 웹 서버(예: Daphne, Uvicorn)와 통신할 수 있도록 설정합니다.

# 기능
# Django 애플리케이션의 ASGI 진입점 역할을 합니다.
# 비동기 작업(예: WebSocket, 실시간 데이터 처리)을 지원합니다.
# Django의 ASGI 애플리케이션을 asgi.application 변수에 할당합니다.
"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()
