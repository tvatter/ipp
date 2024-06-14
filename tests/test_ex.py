import random

import pytest
from hamcrest import assert_that, equal_to


# Define your functions here
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


# Function to generate random test cases for factorial
def generate_random_test_cases(num_cases):
  test_cases = []
  for _ in range(num_cases):
    n = random.randint(0, 10)  # Generate a random integer between 0 and 10
    expected = factorial(
      n
    )  # Calculate the expected result using the correct implementation
    test_cases.append((n, expected))
  return test_cases


# Static test cases
static_test_cases = [
  ("factorial", 0, 1),
  ("factorial", 1, 1),
  ("factorial", 2, 2),
  ("factorial", 3, 6),
  ("factorial", 4, 24),
  ("factorial", 5, 120),
]

# Generate random test cases
random_test_cases = [
  ("factorial", n, expected) for n, expected in generate_random_test_cases(5)
]

# Combine static and random test cases
all_test_cases = static_test_cases + random_test_cases


# Parameterize test cases directly using pytest.mark.parametrize
@pytest.mark.parametrize("fun, n, expected", all_test_cases)
def test_functions(fun, n, expected):
  # Get the function from globals
  func = globals()[fun]
  # Call the function with the parameter
  result = func(n)
  # Create the assert message
  assert_message = f"Calling {fun}({n}) should return {expected}."
  # Use Hamcrest for assertion
  assert_that(result, equal_to(expected), assert_message)