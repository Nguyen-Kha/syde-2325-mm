import smtplib, ssl
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_23_msg(df, i):

    if(pd.isnull(df.loc[i, '2025_2'])):
        message_contents = ''
        message_contents = 'Hi ' + (df[2023][i]).split()[0] + ',\n\n'
        message_contents = message_contents + 'Thank you for signing up to be a mentor. We appreciate you reaching out to the 2025s and '
        message_contents = message_contents + 'helping them feel more at ease with their first year of university. We have paired you with your mentee, '
        message_contents = message_contents + df['2025_1'][i] + '!\n\n'

        message_contents = message_contents + 'Here is what ' + (df['2025_1'][i]).split()[0] + ' had to say about themselves: \n' + df['Bio_1'][i] + '\n'
        message_contents = message_contents + 'You can reach out to them at: ' + df['Email_1'][i] + '.\n\n'

        message_contents = message_contents + 'Please email your mentees in the next couple of days. If you have any questions, reach out to me. '
        message_contents = message_contents + 'Thanks again for volunteering to be a mentor!\n\n'

    # If a 2023 has 2 Mentees
    else:
        message_contents = ''
        message_contents = 'Hi ' + (df[2023][i]).split()[0] + ',\n\n'
        message_contents = message_contents + 'Thank you for signing up to be a mentor. We appreciate you reaching out to the 2025s and '
        message_contents = message_contents + 'helping them feel more at ease with their first year of university. We have paired you with 2 mentees: '
        message_contents = message_contents + df['2025_1'][i] + ' and ' + df['2025_2'][i] + '!\n\n'

        message_contents = message_contents + 'Here is what ' + (df['2025_1'][i]).split()[0] + ' had to say about themselves: \n' + df['Bio_1'][i] + '\n'
        message_contents = message_contents + 'You can reach out to them at: ' + df['Email_1'][i] + '.\n\n'
        message_contents = message_contents + 'Here is what ' + (df['2025_2'][i]).split()[0] + ' had to say about themselves: \n' + df['Bio_2'][i] + '\n'
        message_contents = message_contents + 'You can reach out to them at: ' + df['Email_2'][i] + '.\n\n'

        message_contents = message_contents + 'Please email your mentees in the next couple of days. If you have any questions, reach out to me. '
        message_contents = message_contents + 'Thanks again for volunteering to be a mentor!\n\n'
    
    return message_contents

def generate_25_1_msg(df, i):
    message_contents = ''
    message_contents = 'Hi ' + (df['2025_1'][i]).split()[0] + ',\n\n'
    message_contents = message_contents + 'Thank you for signing up to be a mentee. Your first year of university may be challenging but we\'re '
    message_contents = message_contents + 'here to help you through it! We have paired you with your mentor, ' + df[2023][i] + '.\n\n'
    message_contents = message_contents + 'Here is what ' + (df[2023][i]).split()[0] + ' had to say about themselves: \n' + df['2023_Bio'][i] + '\n\n'
    message_contents = message_contents + 'Your mentor will reach out to you within a week from now. If it has been a week and your mentor has not reached '
    message_contents = message_contents + 'out to you, or if you have any questions or concerns, please email me at kha.nguyen@uwaterloo.ca.'
    
    return message_contents

def generate_25_2_msg(df, i):
    message_contents = ''
    message_contents = 'Hi ' + (df['2025_2'][i]).split()[0] + ',\n\n'
    message_contents = message_contents + 'Thank you for signing up to be a mentee. Your first year of university may be challenging but we\'re '
    message_contents = message_contents + 'here to help you through it! We have paired you with your mentor, ' + df[2023][i] + '.\n\n'
    message_contents = message_contents + 'Here is what ' + (df[2023][i]).split()[0] + ' had to say about themselves: \n' + df['2023_Bio'][i] + '\n\n'
    message_contents = message_contents + 'Your mentor will reach out to you within a week from now. If it has been a week and your mentor has not reached '
    message_contents = message_contents + 'out to you, or if you have any questions or concerns, please email me at kha.nguyen@uwaterloo.ca.'
    
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
            # If a 2023 has a single 2025
            message_to23 = MIMEMultipart()
            message_to23['From'] = sender_email
            message_to23['To'] = df['2023_Email'][i]
            message_to23['Subject'] = 'OFFICIAL - Your SYDE 23/25 Mentor/Mentee Pairing!'
            # message_to23["Bcc"] = sender_email

            message_to23.attach(MIMEText(generate_23_msg(df, i), 'plain'))
            message_to23 = message_to23.as_string()
            server.sendmail(sender_email, df['2023_Email'][i], message_to23) 
            # print(message_to23 + '\n\n\n')
            print('Email Sent To ' + df[2023][i])


            ######   EMAILING THE 2025s   ######
            ###   2025_1   ###
            message_to25_1 = MIMEMultipart()
            message_to25_1['From'] = sender_email
            message_to25_1['To'] = df['Email_1'][i]
            message_to25_1['Subject'] = 'OFFICIAL - Your SYDE 23/25 Mentor/Mentee Pairing!'
            # message_to25_1["Bcc"] = sender_email
            
            message_to25_1.attach(MIMEText(generate_25_1_msg(df, i), 'plain'))
            message_to25_1 = message_to25_1.as_string()
            server.sendmail(sender_email, df['Email_1'][i], message_to25_1)
            # print(message_to25_1 + '\n\n\n')
            print('Email Sent To ' + df['2025_1'][i])

            ###   2025_2   ###
            if(not (pd.isnull(df.loc[i, '2025_2']))):
                message_to25_2 = MIMEMultipart()
                message_to25_2['From'] = sender_email
                message_to25_2['To'] = df['Email_2'][i]
                message_to25_2['Subject'] = 'OFFICIAL - Your SYDE 23/25 Mentor/Mentee Pairing!'
                # message_to25_2["Bcc"] = sender_email

                message_to25_2.attach(MIMEText(generate_25_2_msg(df, i), 'plain'))
                message_to25_2 = message_to25_2.as_string()
                server.sendmail(sender_email, df['Email_2'][i], message_to25_2)
                # print(message_to25_2 + '\n\n\n')
                print('Email Sent To ' + df['2025_2'][i])

if __name__ == "__main__":
    main()