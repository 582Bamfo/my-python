#package is folder containing module
#modules are the files
#from is use to import package/folder. NB import can be use but that will be lengthy
#import is use to import module after after using the from

# there are built-in module / standard lib use in python
import random

print(random.random())

print(random.randint(1,10))

print(random.choice([1,4,8,7]))

#print(random.shuffle( )) look into how to use it


#The sys module in Python provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. It is a built-in module, meaning it is included in the Python Standard Library and is available without the need for installation.

#Key Features and Functions of the sys Module
#Here are some commonly used attributes and methods provided by the sys module:

#Command-Line Arguments (sys.argv):

#sys.argv is a list of command-line arguments passed to a Python script. The first element (sys.argv[0]) is the script name, and subsequent elements are the arguments passed to the script.

import sys
print(sys.argv)

print(sys.modules.keys())

print(" *******************************")
print(sys.path)

# The guessing game
# random_number = randint(int(sys.argv[1]), int(sys.argv[2]))

# while True:
#     try:
#         number = int(
#             input('Please choose a number that falls between those two you just chose: '))
#         if number >= int(sys.argv[1]) and number <= int(sys.argv[2]):
#             if number == random_number:
#                 print("You're a genius!")
#                 break
#     except ValueError:
#         print("Please enter a number")
#         continue





# The true powerhouse of python is Third party developers module/libarary
#You are able to use the by using pip install
#we can use this knowledge base form a website called python package index aka pipy.org

#examples of package is called pyjokes
#It is better to do python package using pycharm/vscode
# pyjokes need to be install first using commandline b4 importting pyjokes
#pip install pyjokes

# import pyjokes
# joke = pyjokes.get_jokes("en", "neutral")


#To solve the issue of diff versionfor diff project, you can use vertual evnt. pipenv+ the version of the package

#try using daytime module

import datetime
print(datetime.time())
print(datetime.time(2,30,1))
print(datetime.date.today())