# accounts/validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomMinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("비밀번호는 최소 %(min_length)d자 이상이어야 합니다."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _("비밀번호는 최소 %(min_length)d자 이상이어야 합니다.") % {
            'min_length': self.min_length
        }
