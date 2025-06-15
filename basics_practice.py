"""
A simple Python script to demonstrate basic concepts:
variables, conditionals, loops, functions, and data structures.
"""

# basics_practice.py
# pylint: disable=C0103
# Variables and data types
name = "Marek"
age = 30
skills = ["Manual Testing", "Python", "Git"]

# Print greeting
print(f"Hello {name}, age {age}!")

# Conditional
if age > 18:
    print("You're an adult.")

# Loop
for skill in skills:
    print(f"- {skill}")

# Function
def add(x, y):
    """Return the sum of two numbers."""
    return x + y

result = add(5, 7)
print(f"5 + 7 = {result}")
