from abc import ABC, abstractmethod
import copy

# Prototype interface
class Shape(ABC):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = None
    
    @abstractmethod
    def clone(self):
        pass

# Concrete prototypes
class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Rectangle [color: {self.color}, x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}]"

class Circle(Shape):
    def __init__(self, radius=0):
        super().__init__()
        self.radius = radius
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Circle [color: {self.color}, x: {self.x}, y: {self.y}, radius: {self.radius}]"

# Client code
def main():
    # Create original objects
    rectangle = Rectangle(5, 10)
    rectangle.color = "blue"
    rectangle.x = 10
    rectangle.y = 20
    
    circle = Circle(15)
    circle.color = "red"
    circle.x = 5
    circle.y = 10
    
    # Clone and modify
    cloned_rectangle = rectangle.clone()
    cloned_rectangle.width = 7
    
    cloned_circle = circle.clone()
    cloned_circle.radius = 20
    
    # Print results
    print("Original rectangle:", rectangle)
    print("Cloned rectangle:", cloned_rectangle)
    print("Original circle:", circle)
    print("Cloned circle:", cloned_circle)

if __name__ == "__main__":
    main() 