"""setting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# 밑에는 실제 사용 예시 (이걸봐라!!)
from rest_framework import permissions

# swagger 문서를 위한 패키지
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 

schema_view = get_schema_view(
    openapi.Info(
        title = '추석 익명 메세지',
        default_version = 'v1.0',
        description = '추석 익명 메세지 API 문서',
        terms_of_service = 'https://127.0.0.1/terms/',
        contact = openapi.Contact(email= "haminsu5@gmail.com"),
        license = openapi.License(name = 'MIT'), # MIT -> 모두가 쓸 수 있는
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.API.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
