#use your IDE TO DO THIS AND VISIT LESSON 17 - SRIPTING


# Using the power of machine to make our life easier.
#learn about processing images
# how to send email
# text messaged
# secure passwod checker to see if password or email has been hacked



#Image processing. This is done by instagram , facebook etc iot save space, makes it looks better , compressing the image

#you can use library and serach for them image processing tool. eg pillow, python image library (PIL) pillow is a pil fork ,
openCV for image and video processing

# pip3 install pillow

#pip install pillow
#Opening an Image:
from PIL import Image

image = Image.open("example.jpg")
image.show()  # Opens the image in the default image viewer

#Saving an Image:
image.save("example_copy.jpg")

#Resizing an Image:
resized_image = image.resize((100, 100))
resized_image.save("example_resized.jpg")


#Rotating an Image:
rotated_image = image.rotate(45)  # Rotate the image by 45 degrees
rotated_image.save("example_rotated.jpg")

#Cropping an Image:
cropped_image = image.crop((100, 100, 400, 400))  # (left, upper, right, lower)
cropped_image.save("example_cropped.jpg")

#Converting an Image to Grayscale:
grayscale_image = image.convert("L")
grayscale_image.save("example_grayscale.jpg")

#Opening and Displaying an Image
image = Image.open("example.jpg")
image.show()  # This will open the image in the default image viewer




https://unsplash.com
#THIS IS FREE WEBSITE YOU CAN DOWLOAD IMAGES TO USE ON YOUR DESKTOP, WEBSITE BACKGROUD ETC

#thumbnail works better if you want to keep the aspect ratio of your image. This works better than resize



#processing pdf file
#pip3 install PyPDF2


#SENDING EMAILS WITH PYTHON
#there is email module built into python
#you can input smtp lib allows to creat smtp server

#sending email using html basis
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = '<to email address>
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<your email address>', '<your password>')
  smtp.send_message(email)
  print('all good boss!')


#Password checker. Check if your password has ever been hack

pip install requests
#https://pypi.org/project/requests/

#You will not be able to run this file here and will need to copy it onto your computer and run it on your machine. 
#You will also need to make sure you have installed the requests module from PyPi (pip install)
import requests
import hashlib
import sys

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times... you should probably change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))



#SMS with python
#use twilio to send 
#Twilio is a cloud communications platform that allows developers to build, scale, and operate real-time communications within their software applications. Twilio provides a suite of APIs (Application Programming Interfaces) that enable features such as:

# Voice: Making and receiving phone calls.
# Messaging: Sending and receiving SMS and MMS messages.
# Video: Enabling video chat and video conferencing.
# Email: Sending and managing email communications through their SendGrid service.
# Authentication: Implementing two-factor authentication and other security features.
# Twilio's services are widely used for customer engagement, notifications, support systems, and various other communication needs. The platform is highly scalable, making it suitable for both small businesses and large enterprises.


# https://www.twilio.com/docs/messaging/quickstart/python


# To send SMS using Twilio, you need to follow these steps:

# Sign up for a Twilio account: If you don't already have one, sign up at Twilio's website.

# Get a Twilio phone number: After signing up, you'll need to purchase a Twilio phone number that you can use to send and receive SMS messages.

# Install the Twilio SDK: Depending on the programming language you are using, install the Twilio helper library. Here’s an example for Python using pip:


 pip install twilio
# Set up your credentials: You'll need your Twilio Account SID and Auth Token, which you can find on your Twilio dashboard.

# Write code to send an SMS: Here's a basic example in Python:

from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello from Twilio!',
    from_='+12345678901',  # Your Twilio phone number
    to='+09876543210'      # The recipient's phone number
)

print(f"Message sent with SID: {message.sid}")




#Another way of notification


# "ntfy" is an open-source notification service that allows you to send notifications to your devices via various methods. It can be used for fun applications like sending funny messages, reminders, or even simple alerts to your phone or other devices. Here’s how you can use ntfy for fun notifications:

# Steps to Use ntfy
# Set Up ntfy:

# Visit the ntfy website for more details and to set up your account if needed.
# Send Notifications via HTTP:

# You can send notifications using a simple HTTP POST request.

# Here’s an example of how to send a notification using curl:


# curl -d "Hello from ntfy.sh!" ntfy.sh/your-topic
# Send Notifications via Python:

# Install the requests library if you don't have it:


# pip install requests
# Use the following Python code to send a notification:


# import requests

# topic = 'your-topic'
# message = 'Hello from ntfy.sh!'

# response = requests.post(f'https://ntfy.sh/{topic}', data=message)

# if response.status_code == 200:
#     print('Notification sent successfully!')
# else:
#     print('Failed to send notification')
# Subscribing to Notifications:

# You can subscribe to notifications on your phone or desktop using the ntfy apps or by visiting the ntfy website and entering your topic.
# Creative Use Cases for Fun:

# Daily Jokes: Set up a script to send a joke daily.
# Random Facts: Send interesting facts at random intervals.
# Friendly Reminders: Send fun reminders to take a break or drink water.
# Game Alerts: Notify when it’s your turn in an online game.
# Example Projects
# Daily Jokes Notification:

# Use an API like the JokeAPI to fetch jokes and send them via ntfy.

# import requests

# def get_joke():
#     response = requests.get('https://v2.jokeapi.dev/joke/Any')
#     joke = response.json()
#     if joke['type'] == 'single':
#         return joke['joke']
#     else:
#         return f"{joke['setup']} ... {joke['delivery']}"

# topic = 'your-topic'
# joke = get_joke()

# response = requests.post(f'https://ntfy.sh/{topic}', data=joke)

# if response.status_code == 200:
#     print('Joke sent successfully!')
# else:
#     print('Failed to send joke')
# Random Fact Notifications:

# Use an API like the Random Facts API to fetch facts and send them via ntfy.

# import requests

# def get_random_fact():
#     response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
#     fact = response.json()
#     return fact['text']

# topic = 'your-topic'
# fact = get_random_fact()

# response = requests.post(f'https://ntfy.sh/{topic}', data=fact)

# if response.status_code == 200:
#     print('Fact sent successfully!')
# else:
#     print('Failed to send fact')
# By integrating ntfy with various APIs and scripting languages, you can create a variety of fun and useful notification systems.






