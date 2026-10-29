# DAY 12: Inheritance

# Inheritance allows a new class (Child) to take on the attributes and methods of an existing class (Parent).
# It promotes code reuse. You don't have to write the same code twice.

print("--- 1. Basic Inheritance ---")

# Parent Class (Base Class)
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child Class (Derived Class)
# The 'Animal' in parentheses means Dog inherits from Animal.
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# The Dog class automatically gets __init__, eat, and sleep from Animal.
my_dog = Dog("Buddy")
my_dog.eat()   # Inherited from Animal
my_dog.sleep() # Inherited from Animal
my_dog.bark()  # Defined in Dog

print("\n--- 2. Overriding Methods ---")
# A child class can replace a method from the parent class.

class Cat(Animal):
    def eat(self):
        # We override the parent's eat method
        print(f"{self.name} the cat is eating fish quietly.")

my_cat = Cat("Whiskers")
my_cat.eat() # Uses Cat's version, not Animal's

print("\n--- 3. Using super() ---")
# 'super()' allows you to call a method from the parent class.
# This is incredibly common in Django!

class Bird(Animal):
    def __init__(self, name, can_fly):
        # Call the parent's __init__ to set the name
        super().__init__(name) 
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying high!")
        else:
            print(f"{self.name} cannot fly.")

eagle = Bird("Eagle", True)
penguin = Bird("Penguin", False)

print(f"{eagle.name} can fly: {eagle.can_fly}")
eagle.fly()
penguin.fly()

print("\n--- 4. Multiple Inheritance (Advanced) ---")
# A class can inherit from multiple parent classes. (Not used as often, but good to know).
class Swimmer:
    def swim(self):
        print("Swimming...")

class Flyer:
    def fly(self):
        print("Flying...")

class Duck(Swimmer, Flyer):
    pass # 'pass' means "do nothing here, just inherit"

donald = Duck()
donald.swim()
donald.fly()