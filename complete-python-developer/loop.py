#A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each element in the sequence. It block looks like the if function

#for item in [1,2,3,4,5,6,]:
 #print(item)

#nested loop
for fax in {1,2,3,4}:
  for hax in ["a", "b", "c","d"]:
    #print(fax)
    #print(hax)
    print(fax,hax)


#Iterables through dictionary
user_name={
  "age":"50",
  "first_name": "dan",
  "hubby": "run"
}

for item in user_name: #this print the key of the object
  print(item)

for k, v in user_name.items(): #printing both k,v
  print(k,v)

for item in user_name.values():#print only values
  print(item)


#counter exercise
counter = 0
my_list =[1,2,3,4,5,6]
for item in my_list:
  counter = item + counter
print(counter)
 # print(len(my_list))


#range() is a built-in function used to generate a sequence of numbers. It's commonly used in conjunction with loops, particularly for loops, to iterate over a specific range of numbers.

print(range(5))
for _ in range(5): # the "_" can rep any variable
  print(_)

#or
for number in range(3): # the "number" can rep  variable
  print(number)

for _ in range(0,10,-1):# -1 is a stepover
  print(_)
#Enumerate

#In Python, the enumerate() function is a built-in function that allows you to iterate over a sequence (such as a list, tuple, or string) while also keeping track of the index of each item in the sequence
#char=("hello")

for i, char in  enumerate("hello there"):
  print(i ,char)

my_list = ["apple", "banana", "orange"]

for index, value in enumerate(my_list):
    print(index, value)

#While loop
# Initialize a variable
count = 0

# Define the while loop condition
while count < 5:
    print("count", count)
    count += 1  # Increment the count variable

print("Loop ended")

#While loop with break
number = 5

while number < 10:
  print("number", number)
  number +=1
  break  # break when number =5
print(f'all done number is equql to {number}')

#While loop with continue
number = 5
while number < 10:
  print("number", number)
  number +=1
  continue
  
print("all done")


# my_test =[1,2,3,4,3]
# duplicate =[]
# for i in my_test:
#   if my_list.count(i) >1:
#   duplicate.append(i)