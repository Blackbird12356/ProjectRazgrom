import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_payment_intent(amount: float, currency: str = 'usd') -> dict:
    """
    Создаёт платёжное намерение в Stripe.
    """
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Сумма в центах
            currency=currency,
        )
        return payment_intent
    except stripe.error.StripeError as e:
        raise Exception(f"Stripe error: {e.user_message}")
