#example additions
def add(arg1,arg2,arg3):
    total =( arg1 + arg2 +arg3)
    return total


#example exponent
def expt(arg1,arg2,):
    total =( arg1**arg2 )
    return total

import time
def order_items(min_order,*args):
    print (f"you have ordered, {min_order}")
    for items in args:
        print(f"you have ordered, {items}")
        time.sleep(2)
    print("enjoy your food")


print(order_items("rice", "pizza"))