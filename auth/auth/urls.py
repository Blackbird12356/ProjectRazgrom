"""
URL configuration for auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Импортируем все нужное
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from contracts.views import ContractViewSet
from payments.views import PaymentViewSet
from django.shortcuts import render


# Временная функция для отображения страницы "Контакты"
def contacts_view(request):
     return render(request, 'contacts.html')   # Здесь можно вернуть полноценный HTML или рендерить шаблон


# Настройка роутера
router = DefaultRouter()
router.register(r'contracts', ContractViewSet, basename='contract')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Подключение маршрутов приложения accounts
    path('', include('accounts.urls')),  # Для упрощения, можно перенаправлять на профиль
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Главная страница
    path('contracts/', include('contracts.urls')),  # Подключение маршрутов для договоров
    path('api/', include(router.urls)),  # Все API доступы через /api/
    path('contacts/', contacts_view, name='contacts'),  # Добавляем маршрут для "Контактов"
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


