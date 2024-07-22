#if condition
x = 21
if x < 30:
    print("inside if block")
    print("x is less than 30")
print("rest of code")

#if/else
x = 31
if x < 30:
    print("inside if block")
    print ("x is less than 30")
else:
    print("x is greater than 30")

#if/elif/else
x = 31
if x < 30:
    print("inside if block")
    print("x is less than 30")
elif x==31:
    print("x is equal to 31")
else:
    print("x is greater than 30")

import time
n = "devops"
for i in n:
    if i == "m":
        print("this is m")
 #       break
    elif i !="s":
        print("the character is", i)
        time.sleep(1)

    else:
        print("end of code")

        
    