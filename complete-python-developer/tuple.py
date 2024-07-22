#tuple are like list but they are immutable ie you cannot sort it , reverse it etc you can access it through index. less flexible.0
#This is use when you do not want anyone to change your statement

my_tuple = (1,2,3,4,5,6,5,7)
print(my_tuple)

new_tuple =("a","b","c")
print(new_tuple)
#print(my_tuple.count())
print(my_tuple.count(5)) # count how many 5s are in the value
print(new_tuple.index("a"))