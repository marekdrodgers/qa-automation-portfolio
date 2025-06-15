# tests/test_calculator.py

import pytest
from src.calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 3) == -3

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(3, 0) == 0
    assert multiply(-2, 2) == -4

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2

    with pytest.raises(ValueError):
        divide(5, 0)  # Expect ValueError for division by zero