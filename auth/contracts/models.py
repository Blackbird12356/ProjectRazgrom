from django.db import models
from django.conf import settings

class Contract(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),      # Ожидает выполнения
        ('completed', 'Completed'), # Выполнен
        ('failed', 'Failed')        # Нарушен
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contracts')
    amount = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name="Сумма")  # Сумма договора
    charity_name = models.CharField(max_length=255, verbose_name="Название Фонда")               # Название фонда
    charity_account = models.CharField(max_length=255,  verbose_name="Реквизиты Фонда")            # Реквизиты фонда
    due_date = models.DateField( verbose_name="Дата завершения")                                 # Дата завершения
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',  verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True)          # Дата создания договора
    goal = models.TextField(null=True, blank=True,  verbose_name="Цель")  # Добавлено поле для цели


    def __str__(self):
        return f"Contract {self.id} by {self.user.username}"
