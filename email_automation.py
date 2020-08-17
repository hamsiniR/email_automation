

import os
import smtplib
# sensitive values have been put as environmental variables
email=os.environ.get('email')
password=os.environ.get('pass')

#We are using the SMTP class to connect to a gmail account
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    # command sent by an email server to identify itself when connecting to another email server to start the process of sending an email
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    #logging in to email
    smtp.login(email,password)
    
    subject="My first Email via python"
    body="yayy"
    # here we are using  fsting for the subject and body of our email
    msg=f'Subject : {subject}\n\n{body}'
   
    #The first attribue is sender email while the second attribute is receiver email
    smtp.sendmail(email,email,msg)
    print('email sent')
