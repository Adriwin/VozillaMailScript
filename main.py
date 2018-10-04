from email_gmail import send_email
from settings import MAX_DISTANCE
from handling_vozilla_api import get_car_distance, get_vozilla_api, get_cars, get_car_plates


if __name__ == '__main__':
    api_response = get_vozilla_api()
    cars = get_cars(api_response)
    send_email(get_car_plates(cars, MAX_DISTANCE), get_car_distance(cars, MAX_DISTANCE))