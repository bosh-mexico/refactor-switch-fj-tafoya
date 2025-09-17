# payment_processors.py
from abc import ABC, abstractmethod

# Clase base abstracta para procesadores de pago
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        """Procesa un pago para un monto dado."""
        pass

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")
        # Add PayPal-specific logic here (e.g., call PayPal API)

class GooglePayProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing GooglePay payment of ${amount:.2f}")
        # Add GooglePay-specific logic here (e.g., call GooglePay API)

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing Credit Card payment of ${amount:.2f}")
        # Add Credit Card-specific logic here (e.g., call Stripe/Adyen API)

class InvalidPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print("Invalid payment mode selected!")