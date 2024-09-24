def score(x,y):
    distance = (x**2 + y**2)**(1/2)
    if distance <= 1:
        return 10
    elif distance <= 5 and distance > 1:
        return 5
    elif distance <= 10 and distance > 5:
        return 1
    else:
        return 0

print(score(0.8,0.8))
print(score(-5,0))
print(score(0,-1))