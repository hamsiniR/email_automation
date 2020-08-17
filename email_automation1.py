


#python -m smtpd -c DebuggingServer -n localhost:1025 
# the above command must be typed on local host

import os
import smtplib

email=os.environ.get('email')
password=os.environ.get('pass')

# set up an email debugging server on local host

with smtplib.SMTP('localhost',1025) as smtp:
    
    subject="My first Email via python"
    body="yayy"
    
    msg=f'Subject : {subject}\n\n{body}'
    #sender -email address
    smtp.sendmail(email,email,msg)
    #print(msg)
    print('email sent')
