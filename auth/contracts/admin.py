from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status', 'due_date')
    list_filter = ('status', 'due_date')
    search_fields = ('user__username', 'charity_name')
