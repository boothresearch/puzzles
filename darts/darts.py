OUTER_RADIUS = 10
MIDDLE_RADIUS = 5
INNER_RADIUS = 1

def score(x, y):
    distance_squared = x**2 + y**2

    if distance_squared <= INNER_RADIUS**2:
        return 10
    elif distance_squared <= MIDDLE_RADIUS**2:
        return 5
    elif distance_squared <= OUTER_RADIUS**2:
        return 1
    else:
        return 0
