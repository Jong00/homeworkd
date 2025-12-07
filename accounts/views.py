from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # main 앱의 home
        else:
            return render(request, 'accounts/login.html', {
                'error': '아이디 또는 비밀번호가 올바르지 않습니다.'
            })

    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()                                  # DB에 새 유저 저장
            login(request, user)                                # 가입 후 자동 로그인
            return redirect("home")                             # 메인 페이지로 이동 (main.urls의 name='home')
    else:
        form = CustomUserCreationForm()

    return render(request, "main/accounts/signup.html", {"form": form})