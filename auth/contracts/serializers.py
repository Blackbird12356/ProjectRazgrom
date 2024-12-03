from rest_framework import serializers
from .models import Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'user', 'amount', 'charity_name', 'charity_account', 'due_date', 'status', 'created_at']
        read_only_fields = ['id', 'status', 'created_at', 'user']
