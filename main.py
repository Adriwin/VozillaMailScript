from email_gmail import send_email
from settings import MAX_DISTANCE
from vozilla_api import get_vozilla_api, get_cars, get_cars_within_distance
import json


if __name__ == "__main__":
    api_response = get_vozilla_api()
    cars = get_cars(api_response)
    cars_nearby = get_cars_within_distance(cars, MAX_DISTANCE)
    if cars_nearby:
        try:
            with open("recent_cars.json", "r") as json_data:
                cars_nearby_saved = json.load(json_data)
            if cars_nearby != cars_nearby_saved:
                f = open("recent_cars.json", "w")
                f.write(json.dumps(cars_nearby))
                f.close()
                send_email(cars_nearby)
        except FileNotFoundError as e:
            print(e)
