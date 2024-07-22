#Error handling in Python is an essential aspect of writing robust and reliable code. It allows you to handle exceptions (errors or unexpected situations) gracefully and take appropriate actions instead of letting your program crash or produce unexpected results.
#Python provides several mechanisms for error handling, including try/except blocks, raising exceptions, and built-in exception classes.

#try/except Blocks:

#The try/except block is the fundamental mechanism for catching and handling exceptions in Python.

try:
  # Code that might raise an exception
  result = 10 / 0
except ZeroDivisionError:
  # Handle the exception
  print("Error: Division by zero is not allowed.")
except Exception as e:
  # Handle other exceptions
  print(f"An error occurred: {e}")
else:
  # Code to be executed if no exception is raised
  print("The result is:", result)
finally:
  # Code to be executed regardless of whether an exception was raised or not
  print("This code will always run.")



print("««««««««««««««««««««««««««««««««««««««««««««««««««")

