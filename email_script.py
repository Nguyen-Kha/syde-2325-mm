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
message = ['hello', 'hello2'] # Will be null, type string

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(username, password)

    for i in range(0, len(df.index)):
        # Send 2025 Mentee 1 email about their Mentor
            # Format Message

        # Send 2023 Mentor email about their Mentee 1

        # Check if there is a Mentee 2 for Mentor
        if(not (pd.isnull(df.loc[i, 'Email_2']))):
            # Send 2025 Mentee 2 email about their Mentor

            # Send 2023 Mentor email about their Mentee 2

    # for i in range(0, len(receiver_emails)):
    #     server.sendmail(sender_email, receiver_emails[i], message[i])
    #     print('Email Sent')

