from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('register/', views.register, name='register'),  # Регистрация
    path('login/', views.login_user, name='login'),  # Вход
    path('logout/', views.logout_user, name='logout'),  # Выход
    path('profile/', login_required(views.profile), name='profile'),   # Личный кабинет
    path('update-profile/', views.update_profile, name='update_profile'),  # Обновление профиля
    path('contract1/', views.contract1, name='contract1'),
    path('contract2/', views.contract2, name='contract2'),
    path('contract3/', views.contract3, name='contract3'),
    path('', views.index, name='index'),  # Главная
    path('about/', views.about, name='about'),  # О нас
    path('contacts/', views.contacts_view, name='contacts'),  # Имя маршрута - contacts

]
