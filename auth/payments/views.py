from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .stripe_service import create_payment_intent
from contracts.models import Contract

class PaymentViewSet(viewsets.ViewSet):
    """
    Обработка платежей через Stripe
    """

    @action(detail=False, methods=['post'])
    def create_intent(self, request):
        """
        Создаёт платёжное намерение для договора.
        """
        contract_id = request.data.get('contract_id')
        try:
            contract = Contract.objects.get(id=contract_id, user=request.user)
            if contract.status != 'pending':
                return Response({'error': 'Оплата возможна только для активных договоров'}, status=400)

            intent = create_payment_intent(amount=float(contract.amount))
            return Response({'client_secret': intent['client_secret']})
        except Contract.DoesNotExist:
            return Response({'error': 'Договор не найден'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
