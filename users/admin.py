from django.contrib import admin

# Register your models here.
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # Используем кастомную форму для добавления пользователя
