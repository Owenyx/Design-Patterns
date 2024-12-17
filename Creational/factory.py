from abc import ABC, abstractmethod

# Abstract Product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Abstract Factory
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

# Concrete Factories
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

class DuckFactory(AnimalFactory):
    def create_animal(self):
        return Duck()

# Client code
def main():
    # Create factories
    factories = {
        "dog": DogFactory(),
        "cat": CatFactory(),
        "duck": DuckFactory()
    }
    
    # Create and test each animal
    for animal_type, factory in factories.items():
        animal = factory.create_animal()
        print(f"{animal_type.capitalize()} says: {animal.speak()}")

if __name__ == "__main__":
    main() 