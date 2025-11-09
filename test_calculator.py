import pytest
from calculator import add, subtract, multiply

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_result_negative():
    assert subtract(3, 5) == -2

def test_add_and_subtract_zero():
    assert add(0, 0) == 0
    assert subtract(0, 0) == 0

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12

def test_multiply_negative_numbers():
    assert multiply(-2, 5) == -10

def test_multiply_with_zero():
    assert multiply(7, 0) == 0

def test_multiply_two_negatives():
    assert multiply(-3, -3) == 9