"""
Main file, everything will run from here
"""
from email_gmail import send_email
from handling_vozilla_api import get_vozilla_api


nokia_coordinates = {
    "latitude": 17.000092,  # x
    "longitude": 51.112571,  # y
}


API = get_vozilla_api()
send_email()

