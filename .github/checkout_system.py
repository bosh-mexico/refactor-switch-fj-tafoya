# checkout_system.py
from payment_modes import PaymentMode
from payment_processors import (
    PaymentProcessor,
    PayPalProcessor,
    GooglePayProcessor,
    CreditCardProcessor,
    InvalidPaymentProcessor
)

# Mapeo de PaymentMode a su respectivo PaymentProcessor
PAYMENT_PROCESSOR_MAP = {
    PaymentMode.PAYPAL: PayPalProcessor(),
    PaymentMode.GOOGLEPAY: GooglePayProcessor(),
    PaymentMode.CREDITCARD: CreditCardProcessor()
}

def checkout(mode: PaymentMode, amount: float):
    """
    Procesa un pago utilizando el modo de pago especificado.
    Esta función está cerrada para modificación y abierta para extensión,
    ya que el mapeo de procesadores se gestiona externamente.
    """
    # Usamos .get() con un valor por defecto para asegurar que siempre haya un procesador.
    # Si 'mode' no se encuentra en PAYMENT_PROCESSOR_MAP (porque no es mapeado o porque no es un PaymentMode),
    # se usará InvalidPaymentProcessor.
    processor: PaymentProcessor = PAYMENT_PROCESSOR_MAP.get(mode, InvalidPaymentProcessor())
    processor.process_payment(amount)

# Example usage
if __name__ == "__main__":
    amount = 150.75

    print("--- Testing Payment Processor (OCP Compliant) ---")
    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)

    # Probando una entrada que NO es un PaymentMode válido.
    # Esto demuestra el comportamiento "default" cuando la entrada es completamente inesperada.
    print("\n--- Testing genuinely invalid input (NOT a PaymentMode instance) ---")
    # Ignoramos la advertencia de tipo porque estamos probando intencionadamente una entrada incorrecta.
    checkout("NotARealPaymentModeString", amount) # type: ignore
    checkout(999, amount) # type: ignore
    checkout(None, amount) # type: ignore

    # Si quieres simular un PaymentMode *existente pero no soportado*,
    # SIN modificar PaymentMode, tendrías que crear una instancia de Enum
    # que no sea de la clase PaymentMode, lo cual es más complejo y no tan útil para esta prueba.
    # Por ahora, con las entradas no-PaymentMode es suficiente para probar el "default".

    print("\n--- End of Test ---")