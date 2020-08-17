# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:53:47 2020

@author: HP
"""



import os
import smtplib

email=os.environ.get('email')
password=os.environ.get('pass')
print(email)
print(password)

with smtplib.SMTP('localhost',1025) as smtp:
    
    subject="My first Email via python"
    body="yayy"
    
    msg=f'Subject : {subject}\n\n{body}'
    #sender -email address
    smtp.sendmail(email,email,msg)
    #print(msg)
    print('email sent')