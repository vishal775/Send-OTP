import random  
import time
import datetime as dt
import string
from twilio.rest import Client
import requests
def msg(password):
    client = Client("AC47902c9d8bcc3e1388601d2595023044", "4c16c8ed8740ff59becf033102ca13b7")
    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(from_='+17706912470',
                           to='+919944446313',
                           body='Your OTP is : '+password)

t = dt.datetime.now()
     
#This code executes for three times
for x in range(3):
    delta = dt.datetime.now()-t
    if delta.seconds >= 0:
        def rand_pass(size):  
         
            # Takes random choices from  
            # ascii_letters and digits  
            generate_pass = ''.join([random.choice( string.ascii_uppercase +
                                                    string.ascii_lowercase +
                                                    string.digits)  
                                                    for n in range(size)])  
                                     
            return generate_pass
        password = rand_pass(10)
        msg(password)
        a=input('Enter the OTP : ')
        if a==password:
            print('Access Granted!!')
            break
        else:
            print('             !!Sorry check the OTP once again!! \n===  The OTP will be sent once again after one minute  ====')
            pass
        
        time.sleep(60)

