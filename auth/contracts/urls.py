from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ContractCreateView.as_view(), name='contract_create'),
    path('list/', views.ContractListView.as_view(), name='contract_list'),
    path('<int:pk>/', views.ContractDetailView.as_view(), name='contract_detail'),
    path('<int:pk>/payment/', views.ContractPaymentView.as_view(), name='contract_payment'),
    path('', views.contract_list, name='contract_list'),  # Список договоров
]
