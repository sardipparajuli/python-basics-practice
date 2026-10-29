# DAY 8: While Loops

# A while loop runs a block of code AS LONG AS a certain condition remains True.
# Use it when you DON'T know exactly how many times you need to loop.

print("--- 1. Basic While Loop ---")
# We MUST create a variable to track the condition before the loop starts.
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # CRITICAL: We must update the variable, or the loop runs forever!

print("Loop finished!")

print("\n--- 2. The 'Break' Statement (Stopping a loop) ---")
# Sometimes you want to loop infinitely until a specific thing happens.
# 'break' forces the loop to stop immediately.
number = 1

while True: # This is an infinite loop!
    print("Checking number:", number)
    if number == 3:
        print("Found 3! Breaking out of the loop.")
        break # Stops the loop completely
    number += 1

print("\n--- 3. The 'Continue' Statement (Skipping an iteration) ---")
# 'continue' skips the rest of the code in the current loop and jumps to the next one.
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue # Skip printing 3
    print("Current num:", num)

print("\n--- 4. Real-World Use Case: Input Validation ---")
# This is how you force a user to enter valid data.
# (Uncomment the code below to test it in your terminal)

"""
user_password = ""

# Keep asking until they type the correct password
while user_password != "secret123":
    user_password = input("Enter the password: ")
    if user_password != "secret123":
        print("Wrong password, try again!")

print("Access Granted!")
"""

print("\n--- 5. Real-World Use Case: Menu System ---")
# You'll use this logic if you ever build a command-line interface.
"""
choice = ""

while choice != "quit":
    print("\n1. Say Hello")
    print("2. Say Goodbye")
    print("Type 'quit' to exit.")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice != "quit":
        print("Invalid choice.")
        
print("Program closed.")
"""