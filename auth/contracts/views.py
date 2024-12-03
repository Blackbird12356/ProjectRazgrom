from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Contract
from .serializers import ContractSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contract
from .forms import ContractForm
from django.urls import reverse



class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Привязываем договор к текущему пользователю
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        # Маркируем договор как выполненный
        contract = self.get_object()
        contract.status = 'completed'
        contract.save()
        return Response({'status': 'Contract marked as completed'})

    @action(detail=True, methods=['post'])
    def fail(self, request, pk=None):
        # Маркируем договор как нарушенный
        contract = self.get_object()
        contract.status = 'failed'
        contract.save()
        return Response({'status': 'Contract marked as failed'})

class ContractCreateView(LoginRequiredMixin, View):
    """
    Представление для создания договора
    """
    def get(self, request):
        form = ContractForm()
        return render(request, 'contracts/contract_form.html', {'form': form})

    def post(self, request):
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.user = request.user  # Привязываем к текущему пользователю
            contract.save()
            return redirect(reverse('contract_payment', args=[contract.id]))
        return render(request, 'contracts/contract_form.html', {'form': form})

class ContractListView(LoginRequiredMixin, ListView):
    """
    Представление для списка договоров
    """
    model = Contract
    template_name = 'contracts/contract_list.html'
    context_object_name = 'contracts'

    def get_queryset(self):
        return Contract.objects.filter(user=self.request.user)

class ContractDetailView(LoginRequiredMixin, DetailView):
    """
    Представление для просмотра деталей договора
    """
    model = Contract
    template_name = 'contracts/contract_detail.html'

class ContractPaymentView(LoginRequiredMixin, View):
    """
    Страница оплаты договора
    """
    def get(self, request, pk):
        contract = get_object_or_404(Contract, pk=pk, user=request.user)
        return render(request, 'contracts/contract_payment.html', {'contract': contract})

def contract_detail(request, id):
    # Получаем договор по ID. Если договора нет, будет ошибка 404
    contract = get_object_or_404(Contract, id=id)
    return render(request, 'contracts/contract_detail.html', {'contract': contract})

def contract_list(request):
    # Получаем договоры текущего пользователя
    contracts = Contract.objects.filter(user=request.user)
    return render(request, 'contracts/contract_list.html', {'contracts': contracts})