# DAY 11: Object-Oriented Programming (OOP)

# A Class is a blueprint. An Object is the actual thing built from the blueprint.
# Example: "Car" is a class. Your specific Honda Civic is an object.

print("--- 1. Creating a Class and an Object ---")
class Dog:
    # __init__ is the constructor. It runs automatically when you create a new object.
    # 'self' refers to the specific object being created.
    def __init__(self, name, breed):
        self.name = name    # Attribute (variable)
        self.breed = breed  # Attribute

    # A Method is just a function inside a class.
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects (instances) from the blueprint
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Accessing attributes
print("Dog 1 name:", dog1.name)
print("Dog 2 breed:", dog2.breed)

# Calling methods
dog1.bark()
dog2.bark()

print("\n--- 2. The 'self' Keyword ---")
# 'self' is how the object refers to itself. 
# When you call dog1.bark(), Python translates it to Dog.bark(dog1).
# That's why 'self' is always the first parameter in a method.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

print("\n--- 3. Using the BankAccount Class ---")
my_account = BankAccount("Sardip", 100)
my_account.deposit(50)
my_account.withdraw(30)
my_account.withdraw(500) # This should trigger the 'Insufficient funds!' message