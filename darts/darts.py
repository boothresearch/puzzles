from math import *
def score(x, y):
    dist = sqrt((x**2)+(y**2))
    if dist <= 1:
        points = 10
    elif dist <= 5:
        points = 5
    elif dist <= 10:
        points = 1
    else: 
        points = 0
    return points
