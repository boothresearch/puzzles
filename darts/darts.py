import math

def score(x, y):
    if math.sqrt(x**2+y**2)>10:
        return 0
    elif math.sqrt(x**2+y**2)>5:
        return 1
    elif math.sqrt(x**2+y**2)>1:
        return 5
    else:
        return 10
