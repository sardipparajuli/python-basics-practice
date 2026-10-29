# DAY 2: Python Operators


# 1. Arithmetic Operators --> Used for basic math calculations.
a = 10
b = 3

print("--- Arithmetic Operators ---")
print("Addition (10 + 3):", a + b)
print("Subtraction (10 - 3):", a - b)
print("Multiplication (10 * 3):", a * b)
print("Division (10 / 3):", a / b)         # Always returns a float (decimal)
print("Floor Division (10 // 3):", a // b) # Divides and drops the decimal (rounds down)
print("Modulus (10 % 3):", a % b)          # Returns the REMAINDER of the division
print("Exponent (10 ** 3):", a ** b)       # 10 to the power of 3 (10 * 10 * 10)

# 2. Comparison (Relational) Operators --> Used to compare two values. Always returns True or False (Boolean).
x = 5
y = 10

print("\n--- Comparison Operators ---")
print("Is x equal to y? (x == y):", x == y)           # Double equals sign! (Single = is for assigning variables)
print("Is x NOT equal to y? (x != y):", x != y)
print("Is x greater than y? (x > y):", x > y)
print("Is x less than y? (x < y):", x < y)
print("Is x greater than or equal to 5? (x >= 5):", x >= 5)

# 3. Logical Operators --> Used to combine conditional statements.
# and, or, not

print("\n--- Logical Operators ---")
is_student = True
has_id_card = False

# 'and' requires BOTH sides to be True
print("Student AND has ID:", is_student and has_id_card) 

# 'or' requires AT LEAST ONE side to be True
print("Student OR has ID:", is_student or has_id_card)

# 'not' reverses the boolean value
print("NOT a student:", not is_student)

# 4. Assignment Operators --> Used to assign values to variables.
print("\n--- Assignment Operators ---")
num = 10
print("Original num:", num)

num += 5  # This is the same as: num = num + 5
print("After += 5:", num)

num -= 3  # This is the same as: num = num - 3
print("After -= 3:", num)

# 5. Membership Operators --> Used to check if a sequence (like a string or list) contains a value.
print("\n--- Membership Operators ---")
my_fruits = ["apple", "banana", "mango"]

print("Is 'apple' in my_fruits?", "apple" in my_fruits)
print("Is 'orange' NOT in my_fruits?", "orange" not in my_fruits)

# You can also use 'in' with strings!
my_name = "Sardip"
print("Does 'Sardip' contain 'sar'?", "sar" in my_name)


# 6. Identity Operators --> Used to compare the memory locations of two objects.
# (is, is not)

print("\n--- Identity Operators ---")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1 # list3 is just another name for list1 (same memory location)

# == checks if the VALUES are the same
print("Are list1 and list2 equal in value? (list1 == list2):", list1 == list2) 

# is checks if they are the EXACT SAME object in memory
print("Are list1 and list2 the same object? (list1 is list2):", list1 is list2)
print("Are list1 and list3 the same object? (list1 is list3):", list1 is list3)