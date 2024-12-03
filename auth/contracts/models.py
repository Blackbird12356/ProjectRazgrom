from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Contract(models.Model):
    """
    Модель договора между пользователем и благотворительным фондом.
    """
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('active', 'Активен'),
        ('completed', 'Завершён'),
        ('failed', 'Не выполнен'),
    ]

    user: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contracts')
    amount: float = models.DecimalField(max_digits=10, decimal_places=2)
    description: str = models.TextField()
    start_date: date = models.DateField(auto_now_add=True)
    end_date: date = models.DateField()
    status: str = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    charity_fund: str = models.CharField(max_length=255)  # Название или реквизиты фонда

    def __str__(self) -> str:
        return f"Договор #{self.id} с {self.user.username}"

