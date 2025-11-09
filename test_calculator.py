import pytest
from calculator import add, subtract

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
