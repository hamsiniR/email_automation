
import os
import smtplib
from email.message import EmailMessage

email=os.environ.get('email')
password=os.environ.get('pass')


contacts=[email,'hamsinishreyas3598@gmail.com']

msg=EmailMessage()
msg['Subject']='My test email'
msg['From']=email
#msg['To']=email
msg['To']=contacts
msg.set_content("yayy")
# to add html directly to our mail 
msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
<style>
body {background-color: powderblue;}
h1   {color: blue;}
p    {color: red;}
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
                    

""",subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
   
    
    smtp.login(email,password)
    
    
    smtp.send_message(msg)
    print('email sent')
