#in python everything is an object. seperation/pactkaging of code/concern so each does what it is good at

#The object will have class associated with all the object hence everything is object because of the class.

#A class is use to instantiate (create) and object(instance) therefore a class is the blueprint for instatiating an object.

#The object can e refer to us the data type. Therefore we can create our own data type by using the idea of oop and class

class BigOject: # class
  pass

#we can therefore instanciate the class to create object/instance
obj1= BigOject()

print(obj1)
print(type(obj1))

#let code our own
#everyclass shoud have init dunder with self defined
#with oop we can create our own attribute and method
#class name shld be uppercase/camel case as seen
class PlayerCharater: 
  def __init__(self, name, age):
    self.name = name #attribute
    self.age = age #attribute
    #self refers to class =PlayerCharater
  #we can create our own method/funtion for our class/object 
  def run(self):
    print("dev")
    return "done"

#We can now instantiate our own obj
player1 =PlayerCharater("dan", 42)
player2 =PlayerCharater("kay", 9)

print (player1.name)
print(player1.age)
print(player1.run())
print(player2.name)


#Class object attribute vrs class attribute
#class object attribute does not change but class attrubte is dynamic as seen above.

class PlayerCharater1: #class name shld be uppercase as seen
  membership =True #class object attribute
  def __init__(self, name, age):
    self.name = name # class attribute
    self.age = age # class attribute
  #we can create our own method/funtion for our class/object 
  def run(self):
    print("dev")
    return "done"

player1 =PlayerCharater1("dan", 42)

print("##printing class object attribute ###")
print(player1.membership)

#setting Default attribute
class PlayerCharater2: 
  def __init__(self, name ="anonymous", age =20):
    self.name = name 
    self.age = age 
   
  def run(self):
    print("dev")
    return "done"

#We can now instantiate our own obj
player1 =PlayerCharater2("dan", 42)
player2 =PlayerCharater2()
print(player2.run)
#Help function help to display details/blueprint about the object/class

#help(player1)

#help([list])




# Exercise Cats Everywhere

# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Answers:
# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat('cat1', 5)
cat2 = Cat('Cat2', 7)
cat3 = Cat('Cat3', 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')


#learn classmethod
#@classmethod


# 4 pillers of OOP

# 1. ENCAPSULARION :binding of data an functions that maupulate the data and we encapsualate into one single box/object  as seen prevoiusly we users can interact with. It help to package data and access the method



# ABTRACTION: hiding info that are not really not needed by user and only give them what is needed
print((1,2,3,1,1).count(1))
#I dont need to know how the count method is contructed. This abstration

#privicy in python is achieve by notifying user with underscore infront of attribute eg _name , _age. this is private abstraction


#INHERITANCE; This allow new obj to take on the property on existing obj


# POLYMORPHISM: The way obj classes can share the same method name but output can be diff base on diff attribute


class Pets():
  animals = []
  def __init__(self, animals):
      self.animals = animals

  def walk(self):
      for animal in self.animals:
          print(animal.walk())

class Cat():
  is_lazy = True

  def __init__(self, name, age):
      self.name = name
      self.age = age

  def walk(self):
      return f'{self.name} is just walking around'

class Simon(Cat):
  def sing(self, sounds):
      return f'{sounds}'

class Sally(Cat):
  def sing(self, sounds):
      return f'{sounds}'


#1 Add another Cat

class Tikachu(Cat):
  def sing(self,sounds):
      return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []
cat1 = Simon('Simon', 10)
cat2 = Sally('Sally', 15)
cat3 = Tikachu('Tikachu', 5)

my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)

#OR my_cats = [Simon('Simon', 10), Sally('Sally', 15), Tikachu('Tikachu', 5)]

#3 Instantiate the Pet class with all your cats use variable my_pets

my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance

my_pets.walk()

# Introspection using the dir fuction or period . to access what the obj/instance has
#The dir function give you access to all what the instance has access to

dev ="hello"
print(dir(dev))  #dir function

print(dev.capitalize()) # introspect with .


# Dunder method: help to use python specific function on obj created thr  our class

class Toys():
  def __init__(self, color, age):
    self.color =color
    self.age =age
    
  def __str__(self): #modify dunder method eg str
    return f"{self.color}"

  def __len__(self): #modify dunder method eg str
    return 5

first_instance= Toys("green", 50)
print(first_instance.age)
print(first_instance.__str__())
print(first_instance.__len__())



#By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class. 
class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
        'name':'Yoyo',
        'has_pets': False,
    }

  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 5

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('yes??')

  def __getitem__(self,i):
      return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])


# Exercise Extending List

class SuperList(list):

    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))

super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
print(issubclass(list, object))


# Inheretance
#MRO - Method Resolution Order
class A:
    num = 10


class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass