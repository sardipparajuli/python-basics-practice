# DAY 6: Loops

# Loops are used to repeat a block of code multiple times.

print("--- 1. For Loop (with range) ---")
# 'range(5)' generates numbers from 0 up to (but not including) 5.
# It's perfect when you know exactly how many times you want to loop.
for i in range(5):
    print("Loop number:", i)

print("\n--- 2. For Loop (iterating a list) ---")
# You can use a for loop to go through every item in a list.
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("I like", fruit)

print("\n--- 3. For Loop (iterating a string) ---")
# You can even loop through every letter in a string!
for letter in "Sardip":
    print(letter)

print("\n--- 4. While Loop ---")
# A while loop runs AS LONG AS the condition is True.
# Be careful! If the condition never becomes False, you get an "infinite loop" and the program crashes.
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1 # We MUST increase the count, or this will run forever!

print("\n--- 5. Break and Continue ---")
# 'break' stops the loop entirely.
# 'continue' skips the rest of the current loop and jumps to the next one.

for i in range(1, 6):
    if i == 3:
        continue # Skip 3
    if i == 5:
        break    # Stop the loop completely at 5
    print("Number:", i)