# DAY 12: Abstraction

# Abstraction means hiding the complex reality while exposing only the necessary parts.
# We use the 'abc' module to create Abstract Base Classes.

from abc import ABC, abstractmethod

print("--- 1. Creating an Abstract Class ---")

class Shape(ABC):
    # By inheriting from ABC, this class becomes an abstract class.
    
    @abstractmethod
    def area(self):
        # This is an abstract method. It has no code inside (just 'pass').
        # Any child class MUST implement this method.
        pass

    @abstractmethod
    def perimeter(self):
        pass

# You CANNOT create an object from an abstract class.
# If you try: my_shape = Shape() -> This will crash with a TypeError!

print("\n--- 2. Implementing the Abstract Class ---")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # We MUST define area() and perimeter(), or Python will throw an error.
    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

# Now we can create objects from the child classes
my_circle = Circle(5)
my_square = Square(4)

print(f"Circle Area: {my_circle.area()}")
print(f"Square Area: {my_square.area()}")