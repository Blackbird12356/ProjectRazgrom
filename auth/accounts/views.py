from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from accounts.models import Profile



def index(request):
    """Главная страница."""
    return render(request, 'index.html')


def register(request):
    """Регистрация пользователя."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    """Вход пользователя."""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли!')
                return redirect('home')  # Измените на ваш маршрут
            else:
                messages.error(request, 'Неверный логин или пароль.')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_user(request):
    """Выход пользователя."""
    logout(request)
    messages.success(request, 'Вы вышли из системы.')
    return redirect('login')


def profile(request):
    """
    Логика отображения личного кабинета.
    """
    # Передаем данные текущего пользователя в шаблон
    if not hasattr(request.user, 'profile'):
     Profile.objects.create(user=request.user)

    return render(request, 'accounts/profile.html', {'user': request.user})


def update_profile(request):
    """
    Обновляет фото профиля пользователя.
    """
    # Убедимся, что у пользователя есть профиль
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        profile = request.user.profile
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()
        return redirect('profile')
    
def contract1(request):
    """Страница договора 1."""
    return render(request, 'accounts/contract1.html')

def contract2(request):
    """Страница договора 2."""
    return render(request, 'accounts/contract2.html')

def contract3(request):
    """Страница договора 3."""
    return render(request, 'accounts/contract3.html')

def about(request):
    """Страница 'О нас'."""
    return render(request, 'accounts/about.html')