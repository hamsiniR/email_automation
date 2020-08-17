# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:22:51 2020

@author: HP
"""
import os
import smtplib
from email.message import EmailMessage
import imghdr

email=os.environ.get('email')
password=os.environ.get('pass')
print(email)
print(password)

contacts=[email,'hamsinishreyas3598@gmail.com']

msg=EmailMessage()
msg['Subject']='My test email'
msg['From']=email
#msg['To']=email
msg['To']=contacts
msg.set_content("yayy")


with open(r"C:\Users\HP\Desktop\pic_dog.jpg","rb") as f:
    file_data=f.read()
    file_type=imghdr.what(f.name)
    file_name=f.name
msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

with open(r"C:\Users\HP\Desktop\Hamsini Ravishankar-Resume.pdf","rb") as f:
    file_data=f.read()
    file_name=f.name
msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
   
    
    smtp.login(email,password)
    
    
    smtp.send_message(msg)
    print('email sent')
