import smtplib
import socket
from email.mime.text import MIMEText


def send_email(plates, distance):
    try:
        f = open("credentials.txt")  # A file which has credentials to gmail account -> username \m password
    except FileNotFoundError as e:
        print(e)
    else:
        gmail_user = f.readline()
        gmail_password = f.readline()
        f.close()

        email_text = 'Hey, \nThe subjects says it all -> go on your Vozilla app and look for the car ' \
                     'with plates: ' + plates + ' and away from you respectively ' + distance + ' [km]'\
                     + '\n\n-Your dearest'
        msg = MIMEText(email_text)
        msg["Subject"] = 'Vozilla nearby'
        msg["From"] = gmail_user
        msg["To"] = gmail_user

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, gmail_user, msg.as_string())
            server.close()
            print("Email sent!")

        except socket.error as e:
            print(e)
