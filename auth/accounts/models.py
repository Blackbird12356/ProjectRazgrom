from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Модель пользователя с возможностью расширения."""
    email = models.EmailField(unique=True)  # Уникальный email вместо username
    REQUIRED_FIELDS = ['email']  # Email обязателен для регистрации

    def __str__(self) -> str:
        return self.username
