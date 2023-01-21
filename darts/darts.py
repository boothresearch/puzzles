import math

def distance(x, y):
    return math.sqrt(x**2 + y**2)

def score(x, y):
    if distance(x, y) <= 1:
        return 10
    elif distance(x, y) <= 5:
        return 5
    elif distance(x, y) <= 10:
        return 1
    else:
        return 0
 