# main/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'main/index/index.html')

def index(request):
    # main/templates/main/index.html
    return render(request, "main/index/index.html")

def login_view(request):
    # main/templates/main/login.html
    return render(request, 'main/login/login.html')

def books(request):
    # main/templates/main/books.html
    return render(request, 'main/books/books.html')

def parts(request):
    # main/templates/main/parts.html
    return render(request, 'main/parts/parts.html')

def board(request):
    # main/templates/main/board.html
    return render(request, 'main/board/board.html')