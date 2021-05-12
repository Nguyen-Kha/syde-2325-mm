from email import message
import smtplib, ssl
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_23_msg(df, i):
    message_contents = ''
    message_contents = 'Hi ' + (df['2023_Name'][i]).split()[0] + ',\n\n'
    message_contents = message_contents + 'Thank you for signing up to help critique resumes. We appreciate you reaching out to the 2025s and '
    message_contents = message_contents + 'helping them with the co-op process. We have paired you with 2 1Bs: '
    message_contents = message_contents + df['2025_1_Name'][i] + ' and ' + df['2025_2_Name'][i] + '!\n\n'

    message_contents = message_contents + 'Name: ' + (df['2025_1_Name'][i]).split()[0] + '\n'
    message_contents = message_contents + 'The roles they are looking for: ' + df['2025_1_Role'][i] + '\n'
    message_contents = message_contents + 'Their email: ' + df['2025_1_Email'][i] + '.\n\n'

    message_contents = message_contents + 'Name: ' + (df['2025_2_Name'][i]).split()[0] + '\n'
    message_contents = message_contents + 'The roles they are looking for: ' + df['2025_2_Role'][i] + '\n'
    message_contents = message_contents + 'Their email: ' + df['2025_2_Email'][i] + '.\n\n'

    message_contents = message_contents + 'Please email your resume critique matches in the next 48 HOURS and arrange something with them, as WaterlooWorks is closing relatively soon. Your pairings may email you their resume through your email ahead of time. If you have any questions, reach out to me. '
    message_contents = message_contents + 'Thanks again for volunteering to help critique resumes!\n\n'

    message_contents = message_contents + 'Cheers,\nKha'

    return message_contents

def generate_25_1_msg(df, i):
    message_contents = ''
    message_contents = 'Hi ' + (df['2025_1_Name'][i]).split()[0] + ',\n\n'
    message_contents = message_contents + 'Thank you for signing up for resume critques. ' + df['2023_Name'][i] + ' from SYDE 2023 will review your resume. '
    message_contents = message_contents + 'They will reach out to you within 48 hours. Feel free to email them a copy of your resume at ' + df['2023_Email'][i] + '.\n\n'

    message_contents = message_contents + 'If it has been 48 hours and ' + df['2023_Name'][i].split()[0] + ' has not reached '
    message_contents = message_contents + 'out to you, or if you have any questions or concerns, please email me at kha.nguyen@uwaterloo.ca.\n\n'

    message_contents = message_contents + 'Cheers,\nKha'
    
    return message_contents

def generate_25_2_msg(df, i):
    message_contents = ''
    message_contents = 'Hi ' + (df['2025_2_Name'][i]).split()[0] + ',\n\n'
    message_contents = message_contents + 'Thank you for signing up for resume critques. ' + df['2023_Name'][i] + ' from SYDE 2023 will review your resume. '
    message_contents = message_contents + 'They will reach out to you within 48 hours. Feel free to email them a copy of your resume at ' + df['2023_Email'][i] + '.\n\n'

    message_contents = message_contents + 'If it has been 48 hours and ' + df['2023_Name'][i].split()[0] + ' has not reached '
    message_contents = message_contents + 'out to you, or if you have any questions or concerns, please email me at kha.nguyen@uwaterloo.ca.\n\n'

    message_contents = message_contents + 'Cheers,\nKha'
    
    return message_contents

def main():
    df = pd.read_excel('')

    smtp_server = 'mailservices.uwaterloo.ca'

    port = 465
    # port = 587
    sender_email = ''
    username = input('username: ')
    password = input('password: ')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(username, password)

        for i in range(0, len(df.index)):

            ###   EMAILING THE 2023s   ###
            message_to23 = MIMEMultipart()
            message_to23['From'] = sender_email
            message_to23['To'] = df['2023_Email'][i]
            message_to23['Subject'] = 'Your S21 SYDE Resume Critique Pairing!'

            message_to23.attach(MIMEText(generate_23_msg(df, i), 'plain'))
            message_to23 = message_to23.as_string()
            server.sendmail(sender_email, df['2023_Email'][i], message_to23) 
            # print(message_to23 + '\n\n\n')
            print('Email Sent To ' + df['2023_Name'][i])

            message_to25_1 = MIMEMultipart()
            message_to25_1['From'] = sender_email
            message_to25_1['To'] = df['2025_1_Email'][i]
            message_to25_1['Subject'] = 'Your S21 SYDE Resume Critique Pairing!'
            
            message_to25_1.attach(MIMEText(generate_25_1_msg(df, i), 'plain'))
            message_to25_1 = message_to25_1.as_string()
            server.sendmail(sender_email, df['2025_1_Email'][i], message_to25_1)
            # print(message_to25_1 + '\n\n\n')
            print('Email Sent To ' + df['2025_1_Name'][i])

            message_to25_2 = MIMEMultipart()
            message_to25_2['From'] = sender_email
            message_to25_2['To'] = df['2025_2_Email'][i]
            message_to25_2['Subject'] = 'Your S21 SYDE Resume Critique Pairing!'

            message_to25_2.attach(MIMEText(generate_25_2_msg(df, i), 'plain'))
            message_to25_2 = message_to25_2.as_string()
            server.sendmail(sender_email, df['2025_2_Email'][i], message_to25_2)
            # print(message_to25_2 + '\n\n\n')
            print('Email Sent To ' + df['2025_2_Name'][i])

if __name__ == "__main__":
    main()