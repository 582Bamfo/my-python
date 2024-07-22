# programs are data that have been modify, store, 

#inte data type and methods
print(round(3.1)) # learn python3 math function google them to learn more

# variables are ways we store data/info in our computer
#varible: best pratcice is to follow snake case(all lowercase with underscore), starts with lower case or underscore, letters, numbers, they are case sensitive, don't override keywords. costant variables are written in capital case, dunder variables are preceeded by double underscore - dont create dundor variables
iq =20
print(iq +2)
print ( type(iq/2) )
print("*********")
print (type("*********") )
a,b,c =1,2,3
print(a)
print(b)

#Expression is a piece of code that produces value ex (iq/2) but statement is the entire line of code ex(user_id = iq/2) the perform the action
iq =20
user_id = iq/2

#Augmented assignment operators and variables
test = 5
print(test)
dev = test -10
print (dev)
print (dev +test)
print (dev +5)
print (type(dev))

#or
test += 15
print(test)

#string is  ordered sequence of character (each charater correspond to an index) or a peice of text/characters with inverted commas/quotation marks. we can use single string '' or double ""or tripple ''''''  '''''' long sting help to create multiple line.  Strings are immutable(create or destroy, cant be changed)

long_set = """
WWWWWW
 o  o
  -
 \"""
 """
print(long_set)
first_name = "Dan"
last_name = "Bamfo"

# string concatenation
print("obour" + "ba")
full_name = first_name + " " +last_name
full_name1 = first_name + last_name
full_name2 = first_name + ", " +last_name
print(full_name)
print(full_name1)
print(full_name2)

#type convertion
print (type(str(100))) # convert int to string
print (type(int(str(100)))) # convert the string back to int

#Escape
#\ = standard escape,  #\t = ( this will add tab space), \n = add a new line
weather = "It\'s sunny."
forecast = "It\'s \"kind of\" foggy"

test_escape= "\t It\'s sunny.\n I hope you have a good day"  #This will include all the ecape funtion
print(weather)
print(forecast)
print (weather,  forecast)
print(test_escape)


#formated string
name = "obour"
age = 50
print(f'hi i am {name} {age} years old')
print(f"hello my name is {name} and I am {age} of age")

print("#####################################")
#String methods or function
quater = "hi there"
print(quater.find("r"))
print(quater.count("i"))
print(quater.capitalize())
print(quater.upper())
print( "-".join(quater).upper())
print("*" .join(quater.lower()))

print("##### Age calculator ########")
#type conversion exercise. program that tells your age based on when you were born
birth_year = input("Please enter your date of birth  ")
age = 2024 - int(birth_year)
print(f'Your age is : {age}')

#Password checker app
print("######### Password checker app#########")
username = input("Enter your username please")
password =  input("Then enter your password")
hidden_password = len(password) * "*"
hidden_username = len(username) * "*"
length_pass = len(password)
print(f'Hi {username} and anomymous {hidden_username} your password is {hidden_password} and it\'s {length_pass} long ')
print("Thank you")

#List: ordered date with index which are mutable. ordered sequence of objects of any type
amazon_cart = ["notebook", "pen", "sharpener", "marker"]
print( amazon_cart)
print(amazon_cart[1])
amazon_cart.insert(1,"ruler")
print (amazon_cart)
amazon_cart.sort() # sort modify the list in place therefore have to print the original list
print(amazon_cart)

print(sorted(amazon_cart)) #creates a new copy of the bucket and sort it. NOT in place
print("notebook"in amazon_cart) # The in function
print("orange"in amazon_cart)
print("marker" in amazon_cart)
amazon_cart.reverse()
a = amazon_cart.reverse()
print(a) # This will print none becos the  method is modify in place and therefore to see the changes you need to print original variable being modified.
print(amazon_cart)
#print(new_amazon)
print("#####################################")
print(range(100))
print("#####################################")
print(list(range(100)))
print("#####################################")
print(len(list(range(100))))
print("#####################################")
#List unpacking
a, b, c, *others, d = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

print(a)
print(b)
print(others)
print(d)

#none: it is a function but can be use to assign variable

weapon ="none"
print (weapon)
