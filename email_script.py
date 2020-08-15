import smtplib, ssl
import pandas as pd

# df = pd.read_csv('')

smtp_server = 'mailservices.uwaterloo.ca'
receiver_emails = ['', '']

port = 465
# port = 587
sender_email = ''
username = input('username: ')
password = input('password: ')
message = ['hello', 'hello2']

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(username, password)
    for i in range(0, len(receiver_emails)):
        server.sendmail(sender_email, receiver_emails[i], message[i])
        print('Email Sent')

