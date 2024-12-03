from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', login_required(views.profile), name='profile'),  # Защищенный маршрут
    path('update-profile/', views.update_profile, name='update_profile'),
    path('contract1/', views.contract1, name='contract1'),
    path('contract2/', views.contract2, name='contract2'),
    path('contract3/', views.contract3, name='contract3'),
    path('', views.index, name='index'),
]
