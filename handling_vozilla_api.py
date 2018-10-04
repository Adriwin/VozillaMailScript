import requests
import math

API_URL = "https://api-client-portal.vozilla.pl//map?objectType=VEHICLE&vehicleStatus=AVAILABLE&vehicleStatus=RESERVED.json"
NOKIA_COORDS = {"latitude": 17.000092, "longitude": 51.112571}


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


def degrees_to_radians(degrees):
    return degrees * math.pi / 180


def coords_in_radians(coords):
    return degrees_to_radians(coords['latitude']), degrees_to_radians(coords['longitude'])


def distance(coords1, coords2):
    EARTH_RADIUS = 6371
    lat1, lon1 = coords_in_radians(coords1) 
    lat2, lon2 = coords_in_radians(coords2)
    
    x = (lon2 - lon1) * math.cos(0.5 * (lat2 + lat1))
    y = lat2 - lat1
    return EARTH_RADIUS * math.sqrt(x * x + y * y)

    
def get_cars_within_distance(cars, max_distance):
    return [car for car in cars if distance(car['location'], NOKIA_COORDS) <= max_distance]


if __name__ == '__main__':
    api_response = get_vozilla_api()
    cars = get_cars(api_response)
    print(get_cars_within_distance(cars, 1000))
