# payment_modes.py
from enum import Enum

class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    BITCOIN = 4 # <--- Añadimos BITCOIN aquí para poder probar un modo no mapeado