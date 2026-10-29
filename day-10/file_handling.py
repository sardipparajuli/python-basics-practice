# DAY 10: File Handling

# Python has built-in functions to read and write files.
# The 'open()' function takes two arguments: the file name and the mode.
# Modes: 'r' (read), 'w' (write - overwrites), 'a' (append - adds to the end), 'x' (create new)

print("--- 1. Writing to a File ('w' mode) ---")
# Note: 'w' will completely overwrite the file if it already exists.
file = open("demo.txt", "w")
file.write("Hello, this is my first line.\n")
file.write("This is the second line.\n")
file.close() # ALWAYS close the file when you are done!
print("File written successfully.")

print("\n--- 2. Appending to a File ('a' mode) ---")
# 'a' adds new content to the end without deleting the old content.
file = open("demo.txt", "a")
file.write("This line was added later.\n")
file.close()
print("File appended successfully.")

print("\n--- 3. Reading a File ('r' mode) ---")
file = open("demo.txt", "r")
content = file.read()
print("File Content:\n" + content)
file.close()

print("\n--- 4. Reading Line by Line ---")
# If a file is huge, you don't want to load it all at once. You can loop through it.
file = open("demo.txt", "r")
for line in file:
    # .strip() removes the extra \n (newline) at the end of each line
    print("Line:", line.strip()) 
file.close()

print("\n--- 5. The BEST way: 'with' statement ---")
# The 'with' statement automatically closes the file for you, even if an error happens. 
# You should ALWAYS use this in real life.
with open("demo.txt", "a") as file:
    file.write("This line was added using the 'with' statement.\n")

with open("demo.txt", "r") as file:
    print("Final File Content:\n" + file.read())