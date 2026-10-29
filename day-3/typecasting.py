# DAY 3: Python Typecasting  (Type Conversion) --> The process of converting one datatype into another.
# For example, changing a string "100" into an integer 100, or a float 99.9 into an integer 99.


# 1. Integer to String
# We use str() to convert numbers into text.
print("--- Int to String ---")
age = 21
print("Original type:", type(age))

age_str = str(age)
print("New type:", type(age_str))
# Now you can combine it with other text!
print("I am " + age_str + " years old.") 

# 2. String to Integer / Float
# We use int() or float() to convert text into numbers.
print("\n--- String to Int/Float ---")
num_str = "100"
print("Original type:", type(num_str))

# If we try: print(num_str + 5) -> This will crash! (Can't add text and number)

num_int = int(num_str)
print("New type:", type(num_int))
print("Math works now:", num_int + 50)

# 3. Float to Integer (Decimal to Whole Number)
# int() simply chops off the decimal part. It does NOT round.
print("\n--- Float to Int ---")
price = 99.99
print("Original:", price)
print("Casted:", int(price)) # Becomes 99, the .99 is lost.

# 4. Integer to Float
# float() adds a .0 to the end.
print("\n--- Int to Float ---")
quantity = 5
print("Casted:", float(quantity)) # Becomes 5.0

# 5. Integer to Boolean
# 0 is False. Every other number is True.
print("\n--- Int to Boolean ---")
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(99):", bool(99))




# Ask the user for their age
user_age = input("Enter your age: ")

# This will crash with a TypeError!
# print("In 10 years, you will be", user_age + 10) 

# This works perfectly:
# print("In 10 years, you will be", int(user_age) + 10)