import smtplib
import socket
from email.mime.text import MIMEText
from settings import USER, PASSWORD, HOST, PORT


def send_email(cars_nearby):
    cars_nearby = "".join("{!s}->{!s}\n".format(k, v) for (k, v) in cars_nearby.items())
    email_text = 'Hey, \nThe subjects says it all -> go on your Vozilla app and look for the car ' \
                 '[plates:distance];\n' + cars_nearby\
                 + '\n\n-Your dearest'
    msg = MIMEText(email_text)
    msg["Subject"] = 'Vozilla nearby'
    msg["From"] = USER
    msg["To"] = USER

    try:
        server = smtplib.SMTP_SSL(HOST, PORT)
        server.ehlo()
        server.login(USER, PASSWORD)
        server.sendmail(USER, USER, msg.as_string())
        server.close()
        print("Email sent!")

    except socket.error as e:
        print(e)
