from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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
