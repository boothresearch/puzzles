def score(x, y):
    distance = (x**2 + y**2) ** (0.5)
    if x==0 and y==0:
        return 10
    elif distance <=1:
        return 10
    elif 1<distance and distance <=5:
        return 5
    elif 5<distance and distance <=10:
        return 1
    elif distance > 10:
        return 0


print(score(1,0))