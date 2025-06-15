# tests/test_calculator.py

"""
Unit tests for calculator.py functions using pytest.
"""

import pytest
from src.calculator import add, subtract, multiply, divide

def test_add():
    """Test addition of two numbers."""
    assert add(2, 3) == 5

def test_subtract():
    """Test subtraction of two numbers."""
    assert subtract(5, 3) == 2

def test_multiply():
    """Test multiplication of two numbers."""
    assert multiply(3, 4) == 12

def test_divide():
    """Test division of two numbers."""
    assert divide(10, 2) == 5

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        divide(5, 0)
