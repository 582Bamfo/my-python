#function that expect 2 arguments
#Function block contain keyword called "def" follow by the function name and arguments in perenthasis

#example1 adding
"""def add(arg1,arg2,arg3):
    total =( arg1 + arg2 +arg3)
    return total

#calling on the function
add (10,3,2)
total =(10+3+2)
print(total)"""

#example exponent
def expt(arg1,arg2,):
    total =(arg1**arg2)
    return total

#calling the method
expt (2,3)
total=(2**3)
print(total)


dev = expt(3,3)
print(dev)


# def dan(x):
#     x=10
#     if x !=10:
#         print("not equal to 10")
#     return(x)


# print(dan(x=6))

import time


"""def order_items(min_order,*args):
    print (f"you have ordered{min_order}")
    for items in args:
        print(f"you have ordered,{items}")
        time.sleep(2)
    print("enjoy your food")

#calling on the function
order_items ("rice","pizza","chicken","buger")"""