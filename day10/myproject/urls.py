# 역할
# URL 라우팅을 담당하며, 클라이언트 요청을 적절한 뷰(view)로 연결합니다.
# 기능
# URL 경로와 뷰를 매핑 (urlpatterns 리스트 사용)
# 앱별 URL 분리를 위해 include() 함수 사용
# 기본적으로 프로젝트 레벨에서 시작하며, 각 앱별로 별도의 urls.py를 가질 수 있습니다.
"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('user/', include('user.urls'))
]
