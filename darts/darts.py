import math

def score(x, y):
    dist_from_center = math.sqrt(x**2 + y**2)
    # Outer radius: 10
    if dist_from_center <= 1:
        return 10
    elif dist_from_center <= 5:
        return 5
    elif dist_from_center <= 10:
        return 1
    else:
        return 0