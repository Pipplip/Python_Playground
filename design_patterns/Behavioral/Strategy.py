"""
Das Strategy-Pattern ist ein Behavioral Design Pattern, das es ermöglicht, 
Algorithmen oder Verhalten austauschbar zu machen, ohne den Code der konsumierenden Klasse zu ändern.

Problemstellung:
Beispiel Einkaufswagensystem.
Kunden können verschiedene Zahlungsmethoden wählen (Kreditkarte, PayPal, Bitcoin).
Die Zahlungslogik soll flexibel und erweiterbar sein, ohne den Einkaufswagen-Code zu verändern.
"""

from abc import ABC, abstractmethod

# ===== Strategy Interface =====
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# ===== Concrete Strategies =====
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"Zahle {amount}€ mit Kreditkarte {self.card_number}.")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"Zahle {amount}€ über PayPal ({self.email}).")

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float):
        print(f"Zahle {amount}€ mit Kryptowährung an {self.wallet_address}.")

# ===== Context Klasse =====
class ShoppingCart:
    def __init__(self):
        self.total_amount = 0
        self.items = []

    def add_item(self, item: str, price: float):
        self.items.append((item, price))
        self.total_amount += price

    def checkout(self, payment_strategy: PaymentStrategy):
        payment_strategy.pay(self.total_amount)

# ===== Client Code =====
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Buch", 29.99)
    cart.add_item("Laptop", 999.99)

    # Zahlung mit Kreditkarte
    credit_card_payment = CreditCardPayment("1234-5678-9012-3456")
    cart.checkout(credit_card_payment)

    # Zahlung mit PayPal
    paypal_payment = PayPalPayment("kunde@example.com")
    cart.checkout(paypal_payment)

    # Zahlung mit Kryptowährung
    payment_method = CryptoPayment("0xABCDEF123456")
    cart.checkout(payment_method)
