# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),              # 메인 페이지
    path('shop/books/', views.books, name='books'),   # 도서 페이지
    path('shop/parts/', views.parts, name='parts'),   # 부품 페이지
    path('board/', views.board, name='board'),        # 게시판 페이지
]
