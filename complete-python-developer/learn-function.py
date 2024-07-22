#function should return something or modify something
#function should return something. The return statement exit the code

def myfun():
  '''
  this is docstring 
  '''
  print("hello")
myfun()
#the docstring help to provide info about the funtion when you start to call it


#functions with parameter and argument 
#parameter = variable , arguements are the values
#functions with positional argument
def mytest(surname,firstname):
 print(f'hello {surname}, {firstname}')
mytest ("bamfo", "daniel")

#default argument
def mytest1(surname = "obour",firstname = "dan"):
 print(f'hello {surname}, {firstname}')
mytest1()


#return in a function
def sum(num1,num2):
 return num1 +num2
total=sum(10,5 )
print(sum(4,5))

def sum1(num1,num2):
   num1 + num2
print(sum1(2,3))

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image! 
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
  for pixel in row:
    if (pixel==1):
       print ("*",end="")
    else:
        print(" ",end="")
  print(" ")

# convert to a function
#Exercise!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
def show_tree():
  for row in picture:
    for pixel in row:
      if (pixel==1):
         print ("*",end="")
      else:
          print(" ",end="")
    print(" ")


show_tree()
show_tree()
show_tree()

#funtion to check if a number is even or not

def is_even(num):
  if num %2 ==0:
   return True
  elif num %2 !=0:
   return False 
print(is_even(4))
print(is_even(3))

# Exercise Functions
# Highest Even: Write a function to find the highest even number from the list.


def highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))


#Walrus operators :=
a = 'helloooooooooo'

if ((n := len(a)) > 10):
    print(f"too long {n} elements")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)
