# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
                                                    # CustomUser: email이 로그인 ID, username은 표시용 이름
        fields = ("email", "username")              # 비밀번호는 password1, password2로 따로 들어감

        labels = {
            "email": "이메일",
            "username": "사용자 이름",
        }