#In Python, a set is a built-in data type used to store a collection of unique elements. Sets are unordered, meaning the elements are not stored in any particular order, and they do not allow duplicate values.

#Sets are defined by enclosing elements within curly braces {}

# set is unordered collection of unique objects

my_set ={"a","b","c","d","d"} #shouldnot contain duplicate 
print(my_set)

mylist=[1,2,3,4,5,6,6,7,7]
#convert list to set : This is use to remove duplicate values eg duplicate email list 
myconvert = set(mylist)
print(myconvert)

my_set.add(100)
print(my_set)
#or
print(my_set.add(200))

lau_set={ 1,2,3,4,5,6,7,8}
kay_set = {1,2,3,4,10} 

print(lau_set.issubset(kay_set))
print(kay_set.issubset(lau_set))
print(lau_set.issuperset(kay_set))
print(lau_set | (kay_set))# .union is also |  
print(lau_set.intersection(kay_set))# can also use &
print(lau_set.difference(kay_set))
print(lau_set.difference_update(kay_set))
