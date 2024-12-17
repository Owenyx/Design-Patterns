from abc import ABC, abstractmethod

# Implementation interface
class Color(ABC):
    @abstractmethod
    def apply_color(self) -> str:
        pass

# Concrete implementations
class RedColor(Color):
    def apply_color(self) -> str:
        return "Red"

class BlueColor(Color):
    def apply_color(self) -> str:
        return "Blue"

class GreenColor(Color):
    def apply_color(self) -> str:
        return "Green"

# Abstraction
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color
    
    @abstractmethod
    def draw(self) -> str:
        pass

# Refined abstractions
class Circle(Shape):
    def draw(self) -> str:
        return f"Drawing Circle in {self.color.apply_color()}"

class Square(Shape):
    def draw(self) -> str:
        return f"Drawing Square in {self.color.apply_color()}"

class Triangle(Shape):
    def draw(self) -> str:
        return f"Drawing Triangle in {self.color.apply_color()}"

# Client code
def main():
    # Create colors
    red = RedColor()
    blue = BlueColor()
    green = GreenColor()
    
    # Create different combinations of shapes and colors
    red_circle = Circle(red)
    blue_square = Square(blue)
    green_triangle = Triangle(green)
    
    # Draw all shapes
    print(red_circle.draw())
    print(blue_square.draw())
    print(green_triangle.draw())
    
    # Change color of existing shape
    red_circle.color = blue
    print(red_circle.draw())

if __name__ == "__main__":
    main() 