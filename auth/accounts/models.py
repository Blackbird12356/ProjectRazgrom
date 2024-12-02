# импортируем что надо
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    """Модель пользователя с возможностью расширения."""
    email = models.EmailField(unique=True)  # Уникальный email вместо username
    REQUIRED_FIELDS = ['email']  # Email обязателен для регистрации

    def __str__(self) -> str:
        return self.username

class Profile(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
   profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


def __str__(self):
    return self.user.username