# testing in Python is crucial to ensure that your code behaves as expected and to catch bugs early in the development process. Python provides several modules and frameworks to facilitate testing, each with its own strengths and features. The most commonly used are unittest, pytest, and doctest.

#unittest Framework
# The unittest module, sometimes referred to as PyUnit, is the built-in testing framework in Python. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.




# Running Tests
# unittest: You can run the tests by executing the script directly or using the python -m unittest discover command to discover and run all tests.
# pytest: Simply run pytest in the terminal to automatically discover and run all tests.
# doctest: Run the script as normal, and the doctest module will execute the tests embedded in the docstrings.
# Summary
# unittest: Built-in, supports complex testing scenarios, but can be more verbose.
# pytest: More powerful and flexible, widely used, and has a rich ecosystem of plugins.
# doctest: Ideal for simple tests and ensuring documentation is accurate.
# Choosing the right testing framework depends on your project requirements and personal preference. For most new projects, pytest is often recommended due to its simplicity and powerful features.

import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=1)

if __name__ == '__main__':
    unittest.main()

# Here's how you can write the same tests using pytest:


import pytest

def add1(a, b):
    return a + b

def test_add():
    assert add1(1, 2) == 3
    assert add1(-1, 1) == 0
    assert add1(-1, -1) == -2

def test_add_floats():
    assert add1(1.1, 2.2) == pytest.approx(3.3, 0.1)

#Here's an example using doctest:
def add(a, b):
  """
  Add two numbers.

  >>> add(1, 2)
  3
  >>> add(-1, 1)
  0
  >>> add(-1, -1)
  -2
  """
  return a + b

if __name__ == '__main__':
  import doctest
  doctest.testmod()
