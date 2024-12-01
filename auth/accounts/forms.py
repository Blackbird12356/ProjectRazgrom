from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    """Форма для регистрации пользователей."""
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    """Форма для входа пользователей."""
    username = forms.CharField(label="Email или имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput)
