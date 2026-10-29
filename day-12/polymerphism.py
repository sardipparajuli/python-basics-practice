# DAY 12: Polymorphism

# Polymorphism allows different classes to share the same method name.
# When you call the method, Python knows exactly which class's version to run.

print("--- 1. Polymorphism with Methods ---")

class Dog:
    def speak(self):
        print("Dog says: Woof!")

class Cat:
    def speak(self):
        print("Cat says: Meow!")

class Cow:
    def speak(self):
        print("Cow says: Moo!")

# Notice that all three classes have a method called 'speak'.
# But they behave differently based on the object.

dog = Dog()
cat = Cat()
cow = Cow()

# We can loop through them and call the SAME method name on each.
for animal in (dog, cat, cow):
    animal.speak()

print("\n--- 2. Polymorphism with Built-in Functions ---")
# Python's built-in functions are also polymorphic!
# The len() function works on strings, lists, and dictionaries.

print(len("Sardip"))          # String (returns number of characters)
print(len(["apple", "banana"])) # List (returns number of items)
print(len({"name": "Sardip", "age": 21})) # Dictionary (returns number of key-value pairs)

print("\n--- 3. Polymorphism with Inheritance (Method Overriding) ---")
# This is the most common use. A child class can override a method from the parent class.

class Bird:
    def fly(self):
        print("Most birds can fly.")

class Penguin(Bird):
    # Penguin inherits from Bird, but overrides the fly() method.
    def fly(self):
        print("Penguins cannot fly, they swim!")

# Even though Penguin is a Bird, calling fly() runs Penguin's version.
generic_bird = Bird()
penguin = Penguin()

generic_bird.fly()
penguin.fly()