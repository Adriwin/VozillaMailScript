import requests
from calculations import distance
from settings import YOUR_COORDS


API_URL = "https://api-client-portal.vozilla.pl//map?objectType=VEHICLE&vehicleStatus=AVAILABLE&vehicleStatus=RESERVED.json"


def get_vozilla_api():
    try:
        response = requests.get(API_URL)
    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema) as e:
        print(e)
    return response.json()


def get_cars(response):
    cars = response['objects']
    if not cars:
        raise RuntimeError('No cars or bad response')
    return cars


def get_cars_within_distance(cars, max_distance):
    cars_within_distance = {}
    for car in cars:
        dist = distance(car['location'], YOUR_COORDS)
        if dist <= max_distance:
            cars_within_distance[car['platesNumber']] = "{} km".format(round(dist, 2))
    return cars_within_distance

