import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from calculator import add, subtract, multiply, divide


def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 0) == 0

def test_subtract_basic():
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    assert subtract(3, 7) == -4

def test_multiply_basic():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_divide_basic():
    assert divide(10, 2) == 5.0

def test_divide_float_result():
    assert divide(7, 2) == 3.5

def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_subtract_floats():
    assert subtract(5.5, 2.0) == 3.5

def test_multiply_negative():
    assert multiply(-3, 4) == -12
