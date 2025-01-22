from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, amount):
        pass

class NoDiscount(Discount):
    def calculate(self, amount):
        return amount

class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def calculate(self, amount):
        return amount * (1 - self.percent / 100)

# Використання
def apply_discount(order_amount, discount: Discount):
    return discount.calculate(order_amount)

# Приклад використання
order_amount = 100
discount = PercentageDiscount(10)  # Знижка 10%
final_amount = apply_discount(order_amount, discount)
print(f"Final amount with discount: {final_amount}")
