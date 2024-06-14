import pytest
from hamcrest import assert_that, equal_to

# Define the student and reference implementations as multiline strings
code_student = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""

code_solution = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""

# Create a student namespace and execute its code
namespace_student = {}
exec(code_student, namespace_student)

# Create a solution namespace and execute its code
namespace_solution = {}
exec(code_solution, namespace_solution)

# Define the function name and test cases
fun_name = "factorial"
test_cases = [
  (0,),
  (1,),
  (2,),
  (3,),
  (4,),
  (5,),
  # Add more test cases as needed
]


# Generate parameterized test cases
@pytest.mark.parametrize("args", test_cases)
def test_functions(args):
  print(namespace_student[fun_name])
  # Retrieve the student and reference functions from their namespaces
  student_func = namespace_student[fun_name]
  reference_func = namespace_solution[fun_name]

  # Call the functions with the parameters
  reference_result = reference_func(*args)
  student_result = student_func(*args)

  # Create the assert message
  assert_message = f"Calling {fun_name}{args} should return {reference_result}"

  # Use hamcrest for assertion
  assert_that(student_result, equal_to(reference_result), assert_message)