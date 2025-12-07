from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),                 # 홈, 메인 화면
    path('accounts/', include('accounts.urls')),    # 로그인/로그아웃
]
