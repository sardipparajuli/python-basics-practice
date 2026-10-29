# DAY 12: Encapsulation

# Encapsulation restricts direct access to some of an object's components.
# It prevents accidental modification of data.

print("--- 1. Public Members (No underscores) ---")
# By default, everything in Python is public. You can access it from anywhere.
class Car:
    def __init__(self):
        self.color = "Red" # Public

my_car = Car()
print("Color:", my_car.color)
my_car.color = "Blue" # Anyone can change it
print("Changed Color:", my_car.color)

print("\n--- 2. Protected Members (Single underscore _) ---")
# A single underscore is a warning to other programmers: "Don't touch this unless you are a subclass!"
# But Python doesn't strictly forbid it.
class Employee:
    def __init__(self):
        self._salary = 50000 # Protected

emp = Employee()
print("Salary:", emp._salary) # It works, but it's considered bad practice.

print("\n--- 3. Private Members (Double underscore __) ---")
# A double underscore makes the variable strictly private.
# Python will throw an error if you try to access it directly from outside the class.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private

    # To access private data, we create public "getter" and "setter" methods.
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid deposit amount")

account = BankAccount(1000)

# print(account.__balance) # ❌ THIS WILL CRASH WITH AN ERROR (AttributeError)

print("Current Balance:", account.get_balance()) # ✅ This works safely
account.deposit(500)
print("New Balance:", account.get_balance())

print("\n--- 4. Getter and Setter using Properties (The Pythonic Way) ---")
# Using @property allows you to access a method like it's a variable.
class User:
    def __init__(self):
        self.__password = "secret123"

    @property
    def password(self):
        return "********" # Returns a masked version for security

    @password.setter
    def password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Error: Password must be at least 8 characters.")

user = User()
print("Password:", user.password) # Calls the getter (returns ********)

user.password = "short" # Calls the setter (fails)
user.password = "newpassword123" # Calls the setter (works)