def factorial(n):
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)