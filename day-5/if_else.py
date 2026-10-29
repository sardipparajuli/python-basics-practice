
# DAY 5: If / Else Statements

# If/Else is used to run different blocks of code based on whether a condition is True or False.
# IMPORTANT: Indentation (spacing) matters in Python! Use 4 spaces (or 1 Tab) for the code inside the if/else blocks.

print("--- Basic If / Else ---")
age = 18

if age >= 18:
    print("You are an adult. You can vote.")
else:
    print("You are a minor. You cannot vote.")

print("\n--- Elif (Else If) ---")
# 'elif' lets you check multiple conditions in order.
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

print("\n--- Multiple Conditions (and / or) ---")
# 'and' requires BOTH to be true.
# 'or' requires AT LEAST ONE to be true.
has_id = True
has_money = False

if has_id and has_money:
    print("You can buy a ticket.")
elif has_id or has_money:
    print("You need one more thing to buy a ticket.")
else:
    print("You cannot buy a ticket.")

print("\n--- Nested If (If inside an If) ---")
# You can put an if statement inside another if statement.
is_logged_in = True
is_admin = False

if is_logged_in:
    print("Welcome to the dashboard!")
    if is_admin:
        print("You have admin access.")
    else:
        print("You have standard user access.")
else:
    print("Please log in first.")