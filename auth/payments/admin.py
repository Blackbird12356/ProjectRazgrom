from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'status', 'created_at')
    search_fields = ('contract__id',)
