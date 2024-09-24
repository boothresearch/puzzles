def score(x, y):
    dist = x**2 + y**2
    if dist <= 1:
        return 10
    elif dist <=25:
        return 5
    elif dist <=100:
        return 1
    else:
        return 0
