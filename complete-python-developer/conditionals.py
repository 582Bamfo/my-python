import time

print("*****Beginning of the IF condtion code *******")
is_old = False
is_licence =   True

if is_old:
  print("old enough to drive!")
elif is_licence:
  print("valid full licence ")
else:
  print("end of verification. Not allow to drive or have valid licence")
time.sleep(1)
print()

print("****** if condition with and********")#both conditions have to be true
DevOps=True
terrform= False
if DevOps and terrform:
  print("Experince with platform engineer" )
else:
  print("Not experienced")


#short curcuiting by using "or" and "and". Python will evaluate the first value and ignore the subsequent one
is_friend =False
is_devops =True

if is_devops or is_friend:
  print("we are best friends")
else:
  print("we are not best friends")


#Ternary operation or conditional expression: operation base on condition been true or not
is_friend = False
can_message = "allow to message" if is_friend else "Not allow to message"
print(can_message)


#Logical operators exercise eg "and", or >,< =
is_magician = False
is_expert = True


if is_magician and is_expert:
  print("You are a master magician")
elif is_magician or is_expert:
  print("At least you tried")
else:
  print("You need magic powers")



a= 10
if a:
  print("hello there")


#Trufy and falsy
test = "asked"
test2 = "quastion"
print (bool(test))
print (bool(test2))
#underneath the hood python convert that to boolen.
#Note, all object are truthy except the following falsy .Please look at the on google 
# 🔸 Falsy Values
# Sequences and Collections:

# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ""
# Empty ranges range(0)
# Numbers

# Zero of any numeric type.
# Integer: 0
# Float: 0.0
# Complex: 0j
# Constants

# None
# False