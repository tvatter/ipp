import pytest
from ipp.ex import factorial


def test_factorial_zero():
  assert factorial(0) == 1


def test_factorial_positive():
  assert factorial(5) == 120


def test_factorial_negative():
  with pytest.raises(ValueError):
    factorial(-5)


def test_factorial_large():
  assert factorial(10) == 3628800