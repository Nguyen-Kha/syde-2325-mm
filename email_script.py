import smtplib, ssl
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

df = pd.read_excel('')

smtp_server = 'mailservices.uwaterloo.ca'
receiver_emails = ['', '']

port = 465
# port = 587
sender_email = ''
username = input('username: ')
password = input('password: ')

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(username, password)

    # for i in range(0, len(df.index)):
    #     # Send 2025 Mentee 1 email about their Mentor
    #         # Format Message

    #     # Send 2023 Mentor email about their Mentee 1

    #     # Check if there is a Mentee 2 for Mentor
    #     if(not (pd.isnull(df.loc[i, 'Email_2']))):
    #         # Send 2025 Mentee 2 email about their Mentor

    #         # Send 2023 Mentor email about their Mentee 2

    # for i in range(0, len(receiver_emails)):
    message_to23 = MIMEMultipart()
    message_to23['From'] = sender_email
    message_to23['To'] = df['2023_Email'][2]
    message_to23['Subject'] = 'Your SYDE 23/25 Mentor/Mentee Pairing!'

    # message_to25_1 = MIMEMultipart()
    # message_to25_1['From'] = sender_email
    # message_to25_1['To'] = sender_email
    # message_to25_1['Subject'] = 'Your SYDE 23/25 Mentor/Mentee Pairing!'

    # message_to25_2 = MIMEMultipart()
    # message_to25_2['From'] = sender_email
    # message_to25_2['To'] = sender_email
    # message_to25_2['Subject'] = 'Your SYDE 23/25 Mentor/Mentee Pairing!'

    # message_to23["Bcc"] = sender_email

    ###   EMAILING THE 2023s   ###
    # If a 2023 has a single 2025
    if(pd.isnull(df.loc[2, '2025_2'])):
        message_contents = 'Hi ' + (df[2023][36]).split()[0] + ',\n\nYour Mentee is ' + df['2025_1'][36] + '. Here is what they said: \n\n'
        message_contents = message_contents + df['Bio_1'][36] + '\n\nThanks for participating. Send me any questions.\n\n'
        message_contents = message_contents + 'Best, \nKha Nguyen'

    # If a 2023 has 2 Mentees
    else:
        message_contents = 'Hi ' + (df[2023][2]).split()[0] + ',\n'
        message_contents = message_contents + 'Thank you for signing up to be a mentor. We appreciate you reaching out to the 2025s and '
        message_contents = message_contents + 'helping them feel more at ease with their first year of university. We have paired you 2 mentees: '
        message_contents = message_contents + df['2025_1'][2] + ' and ' + df['2025_2'][2] + '!\n\n'

        message_contents = message_contents + 'Here is what ' + df['2025_1'][2] + ' had to say about themselves: \n' + df['Bio_1'][2] + '\n'
        message_contents = message_contents + 'You can reach out to them at: ' + df['Email_1'][2] + '.\n\n'
        message_contents = message_contents + 'Here is what ' + df['2025_2'][2] + ' had to say about themselves: \n' + df['Bio_2'][2] + '\n'
        message_contents = message_contents + 'You can reach out to them at: ' + df['Email_2'][2] + '.\n\n'

        message_contents = message_contents + 'Please email your mentees in the next couple of days. If you have any questions, reach out to me. '
        message_contents = message_contents + 'Thanks again for volunteering to be a mentor!\n\n'
        message_contents = message_contents + 'Best,\nKha'
        

    message_to23.attach(MIMEText(message_contents, 'plain'))
    message_to23 = message_to23.as_string()
    server.sendmail(sender_email, sender_email, message_to23)
    print('Email Sent')

