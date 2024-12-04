from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['amount', 'charity_name', 'charity_account', 'due_date', 'goal']
        labels = {
            'amount': 'Сумма',
            'charity_name': 'Название фонда',
            'charity_account': 'Реквизиты фонда',
            'due_date': 'Дата завершения',
            'goal': 'Цель',
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
