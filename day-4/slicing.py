# DAY 4: Slicing

# Slicing is used to grab a CHUNK (multiple items) from a sequence.
# Syntax: variable[start:stop:step]
# IMPORTANT: The 'stop' index is NOT included in the result.

my_name = "Sardip"

print("--- String Slicing ---")
# Grab from index 0 up to (but not including) index 3
print("First 3 letters [0:3]:", my_name[0:3]) # Sar

# If you leave 'start' blank, it starts from the beginning
print("Start to index 4 [:4]:", my_name[:4]) # Sard

# If you leave 'stop' blank, it goes to the very end
print("From index 2 to end [2:]:", my_name[2:]) # rdip

# Slicing with a step (skip letters)
# [start:stop:step]
print("Every 2nd letter [::2]:", my_name[::2]) # Sri

# The famous trick to reverse a string
print("Reversed [::-1]:", my_name[::-1]) # pidraS

print("\n--- List Slicing ---")
fruits = ["apple", "banana", "orange", "mango", "grapes"]

print("First three fruits [:3]:", fruits[:3]) 
print("Middle fruits [1:4]:", fruits[1:4]) 