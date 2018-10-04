import math


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