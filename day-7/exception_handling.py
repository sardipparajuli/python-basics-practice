# DAY 7: Exception Handling (try/except)

# Exceptions are errors that happen while the program is running.
# 'try' block: Code that MIGHT cause an error.
# 'except' block: What to do if the error actually happens (so the program doesn't crash).

print("--- 1. Basic Try/Except ---")
# If you try to divide by zero normally, Python crashes.
# Let's catch the error instead.
try:
    result = 10 / 0
    print("This won't print.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

print("The program continues running normally.")

print("\n--- 2. Catching Multiple Errors ---")
# You can have multiple 'except' blocks for different types of errors.
try:
    number = int("hello") # This will cause a ValueError
except ValueError:
    print("Error: That wasn't a valid number.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

print("\n--- 3. Catching ANY Error (The Safety Net) ---")
# 'Exception' catches absolutely any error that happens inside the try block.
try:
    my_list = [1, 2, 3]
    print(my_list[10]) # This will cause an IndexError
except Exception as e:
    print("Something went wrong!")
    print("The exact error was:", e)

print("\n--- 4. The 'finally' block ---")
# 'finally' runs NO MATTER WHAT (whether there was an error or not).
# It's used for cleanup, like closing a file or a database connection.
try:
    print("Trying to open a file...")
    # pretend file opening code here
except Exception:
    print("An error occurred.")
finally:
    print("This ALWAYS runs. Closing resources.")

print("\n--- 5. The 'else' block ---")
# 'else' runs ONLY IF the 'try' block had NO errors.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Math error.")
else:
    print("Math worked perfectly! The result is:", result)