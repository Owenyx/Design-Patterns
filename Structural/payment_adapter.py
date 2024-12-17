from abc import ABC, abstractmethod
from typing import Dict

# Target Interface - defines how we want to process payments in our system
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> bool:
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        pass

# Adaptee - Third-party payment system with its own interface
class ThirdPartyPayment:
    """Modern payment system with different interface than what we need"""
    def __init__(self):
        self.transactions: Dict[str, float] = {}
        self.counter = 0
    
    def create_payment(self, amount: float) -> str:
        """Initialize a new payment transaction"""
        self.counter += 1
        txn_id = f"TXN_{self.counter}"
        self.transactions[txn_id] = amount
        return txn_id
    
    def execute(self, txn_id: str) -> bool:
        """Complete the payment transaction"""
        return txn_id in self.transactions
    
    def reverse(self, txn_id: str) -> bool:
        """Cancel a payment transaction"""
        if txn_id in self.transactions:
            del self.transactions[txn_id]
            return True
        return False

# Adapter - Makes ThirdPartyPayment work with PaymentProcessor interface
class ThirdPartyAdapter(PaymentProcessor):
    """Adapts the third-party payment system to work with our interface"""
    def __init__(self):
        self.payment = ThirdPartyPayment()
    
    def process_payment(self, amount: float, currency: str) -> bool:
        """Adapt process_payment to use third-party's create and execute methods"""
        txn_id = self.payment.create_payment(amount)
        return self.payment.execute(txn_id)
    
    def refund(self, txn_id: str) -> bool:
        """Adapt refund to use third-party's reverse method"""
        return self.payment.reverse(txn_id)

# Adaptee - Legacy payment system with different interface
class LegacyPayment:
    """Old payment system with different interface than what we need"""
    def __init__(self):
        self.payments: Dict[str, float] = {}
        self.count = 0
    
    def pay(self, amount: float) -> str:
        """Process a payment with legacy system"""
        self.count += 1
        payment_id = f"LEGACY_{self.count}"
        self.payments[payment_id] = amount
        return payment_id
    
    def void(self, payment_id: str) -> bool:
        """Cancel a payment in legacy system"""
        if payment_id in self.payments:
            del self.payments[payment_id]
            return True
        return False

# Adapter - Makes LegacyPayment work with PaymentProcessor interface
class LegacyAdapter(PaymentProcessor):
    """Adapts the legacy payment system to work with our interface"""
    def __init__(self):
        self.legacy = LegacyPayment()
    
    def process_payment(self, amount: float, currency: str) -> bool:
        """Adapt process_payment to use legacy's pay method (USD only)"""
        if currency != "USD":
            return False
        return bool(self.legacy.pay(amount))
    
    def refund(self, txn_id: str) -> bool:
        """Adapt refund to use legacy's void method"""
        return self.legacy.void(txn_id)

# Client code
def process_order(processor: PaymentProcessor, amount: float, currency: str):
    """Process an order using any payment processor that implements our interface"""
    if processor.process_payment(amount, currency):
        print(f"Payment of {amount} {currency} successful")
        if amount > 100:
            processor.refund("TXN_1")
    else:
        print(f"Payment of {amount} {currency} failed")

def main():
    # Test both payment systems through the common interface
    third_party = ThirdPartyAdapter()
    legacy = LegacyAdapter()
    
    # Process various payments with different currencies
    process_order(third_party, 75.50, "USD")  # Should succeed
    process_order(third_party, 150.00, "EUR")  # Should succeed (supports all currencies)
    process_order(legacy, 50.00, "USD")  # Should succeed
    process_order(legacy, 200.00, "EUR")  # Should fail (USD only)

if __name__ == "__main__":
    main() 