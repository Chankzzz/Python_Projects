from email.message import EmailMessage
from py_auth import password,email
import ssl
import smtplib

email_sender=email
email_password=password

email_receiver=input("Enter the Reciver email \n")
# email_receiver="wotepej650@nweal.com"

subject=input("Enter the subject \n")
body=input("Enter the body \n")
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
