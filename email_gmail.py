import smtplib
import socket
from email.mime.text import MIMEText
from settings import user, password, host, port


def send_email(cars_nearby):
    cars_nearby = "".join("{!s}->{!r}\n".format(k, v) for (k, v) in cars_nearby.items())
    email_text = 'Hey, \nThe subjects says it all -> go on your Vozilla app and look for the car ' \
                 '[plates:distance];\n' + cars_nearby\
                 + '\n\n-Your dearest'
    msg = MIMEText(email_text)
    msg["Subject"] = 'Vozilla nearby'
    msg["From"] = user
    msg["To"] = user

    try:
        server = smtplib.SMTP_SSL(host, port)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, user, msg.as_string())
        server.close()
        print("Email sent!")

    except socket.error as e:
        print(e)
