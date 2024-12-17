from abc import ABC, abstractmethod
from typing import List, Optional

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, expiry: str, cvv: str):
        self._card_number = card_number
        self._expiry = expiry
        self._cvv = cvv
    
    def pay(self, amount: float) -> bool:
        print(f"Paying ${amount:.2f} using Credit Card ({self._card_number})")
        # In real implementation, this would process the payment
        return True

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str, password: str):
        self._email = email
        self._password = password
    
    def pay(self, amount: float) -> bool:
        print(f"Paying ${amount:.2f} using PayPal ({self._email})")
        # In real implementation, this would process the payment
        return True

class BankTransferPayment(PaymentStrategy):
    def __init__(self, account_number: str, bank_code: str):
        self._account_number = account_number
        self._bank_code = bank_code
    
    def pay(self, amount: float) -> bool:
        print(f"Paying ${amount:.2f} using Bank Transfer (Account: {self._account_number})")
        # In real implementation, this would process the payment
        return True

# Context
class ShoppingCart:
    def __init__(self):
        self._items: List[tuple[str, float]] = []
        self._payment_strategy: Optional[PaymentStrategy] = None
    
    def add_item(self, item: str, price: float) -> None:
        self._items.append((item, price))
    
    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self._payment_strategy = strategy
    
    def calculate_total(self) -> float:
        return sum(price for _, price in self._items)
    
    def checkout(self) -> bool:
        if not self._items:
            print("Shopping cart is empty!")
            return False
        
        if not self._payment_strategy:
            print("Please set a payment strategy!")
            return False
        
        total = self.calculate_total()
        print("\nProcessing checkout...")
        print("Items:")
        for item, price in self._items:
            print(f"- {item}: ${price:.2f}")
        print(f"Total: ${total:.2f}")
        
        success = self._payment_strategy.pay(total)
        if success:
            self._items.clear()
            print("Checkout completed successfully!")
        else:
            print("Checkout failed!")
        return success

# Client code
def main():
    # Create shopping cart
    cart = ShoppingCart()
    
    # Add some items
    cart.add_item("Python Book", 49.99)
    cart.add_item("Mechanical Keyboard", 159.99)
    cart.add_item("Coffee Mug", 12.99)
    
    # Try checkout without payment strategy
    cart.checkout()
    
    # Checkout with Credit Card
    print("\nTrying Credit Card payment...")
    credit_card = CreditCardPayment("1234-5678-9012-3456", "12/25", "123")
    cart.set_payment_strategy(credit_card)
    cart.checkout()
    
    # Add more items
    cart.add_item("Mouse Pad", 24.99)
    cart.add_item("USB Cable", 9.99)
    
    # Checkout with PayPal
    print("\nTrying PayPal payment...")
    paypal = PayPalPayment("user@example.com", "password123")
    cart.set_payment_strategy(paypal)
    cart.checkout()
    
    # Add another item
    cart.add_item("Headphones", 89.99)
    
    # Checkout with Bank Transfer
    print("\nTrying Bank Transfer payment...")
    bank_transfer = BankTransferPayment("987654321", "BANKCODE123")
    cart.set_payment_strategy(bank_transfer)
    cart.checkout()

if __name__ == "__main__":
    main() 