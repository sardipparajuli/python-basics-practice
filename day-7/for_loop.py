# DAY 7: For Loop (Advanced)


# 1. Enumerate
# If you need BOTH the index and the item, use enumerate().
print("--- 1. Enumerate ---")
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 2. Looping through a Dictionary
# By default, looping a dictionary gives you the KEYS.
print("\n--- 2. Dictionary Loops ---")
person = {"name": "Sardip", "age": 21, "city": "Kathmandu"}

# Just keys
for key in person:
    print("Key:", key)

# Keys and Values using .items()
print("With .items():")
for key, value in person.items():
    print(f"{key}: {value}")

# 3. Nested Loops (A loop inside a loop)
print("\n--- 3. Nested Loops ---")
# For every number in the outer loop, the inner loop runs completely.
for i in range(1, 3):
    for j in range(1, 3):
        print(f"Outer: {i}, Inner: {j}")

# 4. List Comprehension (A shortcut for making lists)
# This is a very "Pythonic" way to do a loop and create a list in one line.
print("\n--- 4. List Comprehension ---")
# Normally you'd do: 
# squares = []
# for x in range(5): squares.append(x**2)

squares = [x**2 for x in range(5)]
print("Squares:", squares)