# DAY 4: Indexing

# Indexing is used to grab a SINGLE item from a sequence (like a string or list).
# Python uses Zero-based indexing, meaning the first item is at position 0.

my_name = "Sardip"
# Indexes:   0 1 2 3 4 5
# Letters:   S a r d i p

print("--- String Indexing ---")
print("First letter (index 0):", my_name[0])
print("Third letter (index 2):", my_name[2])

# Negative indexing starts counting from the end
print("Last letter (index -1):", my_name[-1])
print("Second to last (index -2):", my_name[-2])

print("\n--- List Indexing ---")
fruits = ["apple", "banana", "orange", "mango"]
# Indexes:     0        1         2         3

print("First fruit (index 0):", fruits[0])
print("Last fruit (index -1):", fruits[-1])