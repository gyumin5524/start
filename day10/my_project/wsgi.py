# 역할
# Django 프로젝트가 동기식 웹 서버(예: Gunicorn, uWSGI, Apache)와 통신할 수 있도록 설정합니다.
# 기능
# Django 애플리케이션의 WSGI 진입점 역할을 합니다.
# wsgi.application 변수에 Django의 WSGI 애플리케이션을 할당합니다.
# 프로덕션 환경에서 주로 사용됩니다.
"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
