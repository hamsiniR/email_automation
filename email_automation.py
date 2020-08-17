# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:22:52 2020

@author: HP
"""

import os
import smtplib

email=os.environ.get('email')
password=os.environ.get('pass')
print(email)
print(password)

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
   
    smtp.login(email,password)
    
    subject="My first Email via python"
    body="yayy"
    
    msg=f'Subject : {subject}\n\n{body}'
   
    smtp.sendmail(email,email,msg)
    print('email sent')