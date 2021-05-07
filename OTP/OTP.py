import random  
import time
import datetime as dt
import string
from twilio.rest import Client
import requests
def msg(password):
    num='+91'+'YOUR_PHONE_NUMBER'
    client = Client("YOUR_ACCOUNT_SID", "YOUR_AUTH_TOKEN")
    client.messages.create(from_='YOUR_TRIAL_NUMBER',
                           to=num,
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

