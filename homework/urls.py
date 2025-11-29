from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('main.urls')),        # 메인 페이지 URL
    path('', include('accounts.urls')),    # 로그인/로그아웃 URL
]
