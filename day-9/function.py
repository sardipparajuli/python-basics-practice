# DAY 9: Functions

# A function is a block of organized, reusable code that is used to perform a single, related action.
# We use the 'def' keyword to define a function.

print("--- 1. Basic Function ---")
# This function just prints something. It takes no inputs and returns nothing.
def say_hello():
    print("Hello, brochacho!")
    print("Welcome to Python functions.")

# To run the function, we have to "call" it by its name.
say_hello()
say_hello() # We can call it as many times as we want!

print("\n--- 2. Functions with Parameters (Arguments) ---")
# Parameters are the variables listed inside the parentheses.
# They allow us to pass data into the function.
def greet_user(name):
    print(f"Hello, {name}! How are you today?")

greet_user("Sardip")
greet_user("Diya Ma'am")

print("\n--- 3. Functions with Multiple Parameters ---")
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

add_numbers(5, 10)
add_numbers(100, 250)

print("\n--- 4. The 'return' Statement ---")
# Instead of just printing, a function can 'return' a value back to wherever it was called.
# This is crucial! It allows you to save the result in a variable.
def multiply(a, b):
    return a * b

# We can save the returned value in a variable
answer = multiply(4, 5)
print("The returned answer is:", answer)

# Or we can print it directly
print("Directly printing:", multiply(10, 10))

print("\n--- 5. Default Parameters ---")
# You can give a parameter a default value. If the user doesn't provide it, the default is used.
def make_pizza(size, topping="cheese"):
    print(f"Making a {size} inch pizza with {topping}.")

make_pizza("12") # Uses the default topping
make_pizza("14", "mushrooms") # Overrides the default topping

print("\n--- 6. Why use 'return' instead of 'print'? ---")
# If a function just prints, you can't do math with the result.
# If a function returns, you can use the output for other things.
def square(n):
    return n * n

# Because it returns, we can nest it inside other functions:
print("The square of the square of 3 is:", square(square(3)))