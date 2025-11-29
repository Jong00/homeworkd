from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                # 루트(/)에 index 연결
    path('login/', views.login_page, name='login'),     # login 화면
]
