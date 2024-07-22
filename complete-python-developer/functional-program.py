#function is like varibles which can be use anywhere


# It is separation of concerns. one important pillar is called pure function. there is sepation of data and behaviour of data. It separate data and funtion unlike oop where data and function are togehter.

# Pure function: shld not affect the outside world/no effect. when give same input it should produce the same output. No buggie code , 

def multiply_by2(li):
  new_list =[]
  for item in li:
    new_list.append(item*2)
  return new_list

print(multiply_by2([1,2,3]))


#Further understanding of map, ruduce, filter, zip function

# MAP
# The map() function in Python is a built-in function that applies a given function to each item in an iterable (like a list, tuple, or string) and returns a map object, which is an iterator containing the results. It's a useful tool for applying operations to all elements of a sequence without writing an explicit loop.
#The basic syntax of map() is:
#pythonCopy codemap(function, iterable[, iterable2, ...])

# Convert all strings to uppercase
names = ["alice", "bob", "charlie"]
uppercase_names = map(str.upper, names)
print(list(uppercase_names))# Output: ['ALICE','BOB', 'CHARLIE']


#Using map() with a user-defined function:
# Square each number
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# Add 10 to each number
numbers = [1, 2, 3, 4, 5]
added_numbers = map(lambda x: x + 10, numbers)
print(list(added_numbers))  # Output: [11, 12, 13, 14, 15]





#FILTER FUNCTION
#The filter() function in Python is a built-in function that constructs an iterator from elements of an iterable for which a function returns True. It's used to filter out elements from a sequence based on a given predicate (a function that returns a boolean value).

# The basic syntax of filter() is:
# pythonCopy codefilter(function, iterable)

# function: A function that tests each element in the iterable. It should return True for elements to be included and False for elements to be excluded. If None is used instead of a function, the identity function is assumed, which means elements that are False or equivalent to False (like 0, "", [], None) will be removed.
# iterable: An iterable object like a list, tuple, string, etc.
# Filter out even numbers
def is_odd(n):
    return n % 2 != 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # Output: [1, 3, 5, 7, 9]

def is_multiples(m): #is multiple of 2 with 6 as answer
 # for item in m:
   return m*2==6
number = [1, 2, 3]
test_filter =map(is_multiples, number)
test_filter1 = filter(is_multiples, number)
print(list(test_filter))
print(list(test_filter1))


# Filter out dictionaries with value < 30
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]
adults = filter(lambda person: person['age'] >= 30, people)
print(list(adults))  # Output: [{'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Filter out strings with length less than 6
words = ['python', 'java', 'c++', 'javascript', 'go']
long_words = filter(lambda x: len(x) >= 6, words)
print(list(long_words))  # Output: ['python', 'javascript']

print()

old_number = [1 ,2, 3, 4, 5, 6]
check_old =filter(lambda n:n%2!=0, old_number)
print(list(check_old))


#The zip() function in Python is a built-in function that aggregates elements from each of the input iterables into tuples. It's commonly used to combine two or more lists, tuples, or other sequences element-wise.
# The basic syntax of zip() is:
# pythonCopy codezip(*iterables)

# *iterables: One or more iterables (like lists, tuples, strings, etc.).
print()
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']

zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# Note: 'd' is ignored because list1 is shorter
print()
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

tes_zip =  zip(names, ages)
print(list(tes_zip))

print()

names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# Output:
# Alice is 24 years old.
# Bob is 50 years old.
# Charlie is 18 years old.

print()
# REDUCE:
# The reduce() function in Python is part of the functools module. It's a higher-order function that applies a function of two arguments cumulatively to the items of a sequence, reducing the sequence to a single value. It's particularly useful when you want to perform some computation on a list and reduce it to a single result.
# The basic syntax of reduce() is:
# pythonCopy codefrom functools import reduce

# reduce(function, iterable[, initializer])

# function: A function that takes two arguments. It's applied to the first two items of the sequence, then to the result and the next item, and so on.
# iterable: An iterable object like a list, tuple, string, etc.

from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15

# Equivalent to:
# total = 1 + 2 = 3
# total = 3 + 3 = 6
# total = 6 + 4 = 10
# total = 10 + 5 = 15
print("*************************************")
def multiply(x, y):
  return x * y

numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)
print(product)  # Output: 24

print("*************************************")
numbers = [3, 7, 2, 9, 5]
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(max_num)  # Output: 9

print("*************************************")
from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))


# LAMBDA EXPRESSIONS
#A lambda function in Python is a small, anonymous function that can have any number of arguments but can only have one expression. THIS IS ONLY USE ONCE AND DOES NOT NEED TO BE STORE IN MEMORY THEREFOR def is not needed It's also known as an anonymous function because it doesn't have a name like regular functions defined with the def keyword. Lambda functions are defined using the lambda keyword.
# The basic syntax of a lambda function is:
# pythonCopy codelambda arguments: expression

# arguments: Zero or more arguments, separated by commas.
#expression: A single expression that gets evaluated and returned.
# A lambda function that adds 10 to its argument
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15

#Lambda with multiple arguments:

# A lambda function that returns the larger of two numbers
max_of_two = lambda x, y: x if x > y else y
print(max_of_two(10, 20))  # Output: 20

#Using lambda with map():

# Square each number in a list
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]


#Comprehensions in Python are a concise and efficient way to create lists, dictionaries, sets, and generators in a single line of code. They provide a compact syntax for generating sequences based on existing sequences or other iterable objects. Python supports four types of comprehensions:

# List Comprehensions
# Dictionary Comprehensions
# Set Comprehensions
# Generator Expressions (not technically a comprehension, but similar syntax)
# List Comprehensions:

# Create lists based on existing lists or other iterables.
# Syntax: [expression for item in iterable if condition]

# Square numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Nested list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]