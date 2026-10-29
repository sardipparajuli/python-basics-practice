# DAY 9 (Part 2): *args and **kwargs

# Sometimes, you don't know how many arguments will be passed to your function.
# *args allows you to pass a variable number of NON-KEYWORD (positional) arguments.
# **kwargs allows you to pass a variable number of KEYWORD (named) arguments.

print("--- 1. *args (Non-Keyword Arguments) ---")
# The * means it will accept any number of arguments and pack them into a TUPLE.
def print_students(*args):
    print("Type of args:", type(args))
    print("The students are:")
    for student in args:
        print("-", student)

# We can pass 2 students, or 5 students, or 10!
print_students("Sardip", "Rajib")
print("\n")
print_students("Sardip", "Rajib", "Samuel", "Manjar")

print("\n--- 2. **kwargs (Keyword Arguments) ---")
# The ** means it will accept any number of named arguments and pack them into a DICTIONARY.
def print_profile(**kwargs):
    print("Type of kwargs:", type(kwargs))
    print("User Profile:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Notice we pass them like key=value
print_profile(name="Sardip", age=21, city="Kathmandu")

print("\n--- 3. Using BOTH *args and **kwargs ---")
# You can use both! Just remember the order: standard args first, then *args, then **kwargs.
def make_order(item, *extras, **details):
    print(f"Main item: {item}")
    
    if extras:
        print("Extras:")
        for extra in extras:
            print("-", extra)
            
    if details:
        print("Order Details:")
        for key, value in details.items():
            print(f"{key}: {value}")

# Calling the function
make_order("Burger", "Fries", "Coke", customer_name="Sardip", table_number=5)