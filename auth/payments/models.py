from django.db import models
from django.contrib.auth.models import User
from contracts.models import Contract
from datetime import datetime

class Payment(models.Model):
    """
    Модель платежа, связанная с договором.
    """
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('completed', 'Завершён'),
        ('failed', 'Неудачный'),
    ]

    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    contract: Contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='payments')
    amount: float = models.DecimalField(max_digits=10, decimal_places=2)
    payment_intent_id: str = models.CharField(max_length=255)  # Идентификатор платежа в системе Stripe
    status: str = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Платеж #{self.id} для договора #{self.contract.id}"
