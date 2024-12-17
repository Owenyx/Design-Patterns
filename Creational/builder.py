from abc import ABC, abstractmethod

# Product
class Pizza:
    def __init__(self):
        self.parts = []

    def add(self, part: str):
        self.parts.append(part)

    def show(self) -> str:
        return f"Pizza with: {', '.join(self.parts)}"

# Abstract Builder
class PizzaBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def add_dough(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_toppings(self):
        pass

    @abstractmethod
    def get_result(self) -> Pizza:
        pass

# Concrete Builder
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = None
        self.reset()

    def reset(self):
        self.pizza = Pizza()

    def add_dough(self):
        self.pizza.add("thin crust dough")

    def add_sauce(self):
        self.pizza.add("tomato sauce")

    def add_toppings(self):
        self.pizza.add("mozzarella")
        self.pizza.add("fresh basil")

    def get_result(self) -> Pizza:
        return self.pizza

# Director
class Waiter:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.reset()
        self.builder.add_dough()
        self.builder.add_sauce()
        self.builder.add_toppings()

# Client code
def main():
    waiter = Waiter()
    margherita_builder = MargheritaPizzaBuilder()
    
    waiter.set_builder(margherita_builder)
    waiter.construct_pizza()
    
    pizza = margherita_builder.get_result()
    print(pizza.show())

if __name__ == "__main__":
    main() 