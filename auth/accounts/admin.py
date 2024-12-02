from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Регистрация модели CustomUser в админке."""
    list_display = ('username', 'email', 'is_staff', 'is_active')  # Поля для отображения
    search_fields = ('username', 'email')  # Поля для поиска
    list_filter = ('is_staff', 'is_active')  # Фильтры
