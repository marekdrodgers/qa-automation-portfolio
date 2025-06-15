# src/calculator.py

"""
Simple calculator functions for addition, subtraction,
multiplication, and division.
"""

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the division of x by y. Raises ValueError on division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
