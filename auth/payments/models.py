from django.db import models
from contracts.models import Contract

class Payment(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='payment') #Связь с договором
    payment_id = models.CharField(max_length=255)          # ID транзакции в платёжной системе
    status = models.CharField(max_length=50)               # Статус платежа (успешен, провален)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Contract {self.contract.id} - {self.status}"
