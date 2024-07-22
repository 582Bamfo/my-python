#Decorators in Python are a way to modify or extend the behavior of a function without changing its source code. They are essentially higher-order functions that take one or more functions as input, add some functionality, and return a new function.
#Decorators are defined using the @ symbol followed by the name of the decorator function, which is then placed just before the function definition. When the decorated function is called, it is first passed to the decorator function, which can perform some operations and then return either the same function or a new one.

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
# Output:
# Calling function add_numbers
# Function add_numbers returned 5

print("«««««««««««««««««««««««««««««««««««««««««««««««««««")
from functools import lru_cache

def cache_result(func, max_size=128):
    cached_func = lru_cache(maxsize=max_size)(func)
    return cached_func

@cache_result
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))  # Calculated and cached
print(fibonacci(50))  # Retrieved from cache


print("«««««««««««««««««««««««««««««««««««««««««««««««««««")
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    "name": "Sorna",
    "valid": True,  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")

    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)