#generators.

#in Python, generators are a type of iterable, like lists or tuples. Unlike lists, however, generators do not store their contents in memory; instead, they generate values on the fly and thus are more memory-efficient. Generators are particularly useful when dealing with large datasets or streams of data where you do not need all the data at once.

#Creating Generators
# Generator Functions:
# These are similar to regular functions but use the yield statement to return values one at a time.

def simple_generator():
  yield 1
  yield 2
  yield 3

gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


print("************************")

def countdown(n):
  while n > 0:
      yield n
      n -= 1

cd = countdown(5)
for number in cd:
  print(number)

#generators are much more performant than lists. (i.e range > list in performance.)

#So generators are really, really useful when calculating large sets of data.

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, *kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(10): #it finishes after.
        i*5

long_time()
print()

@performance
def long_time2():
    print('2')
    for i in list(range(10)): #it took longer.
        i*5

long_time2()
print()


print("************************")

def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      iterator*5
      next(iterator)
    except StopIteration:
      break


class MyGen:
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last
    MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

gen = MyGen(1,100)
for i in gen:
    print(i)


print("************************")

# def fib(number):
#     n1 = 0
#     n2 = 1
#     for i in range(number):
#         yield n1
#         temp = n1
#         n1 = n2
#         n2 = temp + n2


# for x in fib(10000):
#     print(x)