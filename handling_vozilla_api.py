"""
File in which I will handle the API
"""
import requests


def get_vozilla_api():
    # url = "https://api-client-portal.vozilla.pl//map?objectType=VEHICLE^&vehicleStatus=AVAILABLE^&vehicleStatus=RESERVED.json"
    # url = "https://api-client-portal.vozilla.pl//map?objectType=ZONE"
    url = "https://jsonplaceholder.typicode.com/todos/1"
    # url = "http://api.open-notify.org/astros.json"
    # url = ""
    try:
        response = requests.get(url)
    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema) as e:
        print(e)
    else:  # When try: wont raise an exception -> else will happen
        data = response.json()
        print(data)
        # return data
    # finally:  # This will run no matter what will happen above
    #     print("Runs always")


get_vozilla_api()
