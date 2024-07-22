#Dictionary is an unordered key value pair of data
# A dictionary is a collection of key-value pairs.
# Dictionaries are defined by enclosing key-value pairs within curly braces {} and separating each pair by a colon : (key-value pairs are separated by commas ,).
# Keys within a dictionary must be unique, but the values can be duplicates.
# Dictionaries are mutable, meaning you can add, remove, or modify key-value pairs.
# Dictionaries are used to store and retrieve data based on keys. You can look up values by their corresponding keys efficiently

user_names = {
             "user1": "Dan", 
              "user2": "Lin",
              "user3": "lau"
             }

print(user_names)
print(user_names["user1"])
print(user_names["user2"])
#print(user_names["Lin"])
#print(user_names["lau"])
print(user_names["user1"][:2])
#dic methods
print(user_names.keys()) #to get keys
print(user_names.values()) # to get values
print(user_names.keys())
print(user_names.get("age")) # age does not exit. To prevent the error use .get
print(user_names.get("age","20")) #create another key,v which doesnot exit in the dic

#Alternative of creating Dictionary

# new_user = dict(user4 ="kay" )
# print(new_user)

print("lau" in user_names) #default in works with keys
print("user2" in user_names)
print("lau" in user_names.values())
print("lau" in user_names.keys())
print("user1" in user_names.keys())

print(user_names.items()) # item grab all the data
print(user_names.items())
print(user_names.pop("user2")) # return the value of the removed key
print(user_names.popitem()) #remove the last item
#print(user_names.popitem(user2))
print(user_names) #print the last item after the 2 pop cmd above

user_names.update({"user2":"kay"})
print(user_names)


