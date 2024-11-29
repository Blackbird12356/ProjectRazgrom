from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации нового пользователя."""

    class Meta:
        model = CustomUser
        fields = ('email', 'username')  # Поля, которые будут отображаться в форме

    def clean_email(self):
        """Проверяем, что email уникален."""
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email


class CustomAuthenticationForm(AuthenticationForm):
    """Форма для входа пользователя."""
    
    def confirm_login_allowed(self, user):
        """Дополнительная проверка статуса пользователя."""
        if not user.is_active:
            raise forms.ValidationError(
                "Этот аккаунт неактивен. Обратитесь в службу поддержки.",
                code='inactive',
            )

