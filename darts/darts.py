def score(x, y):
    if x**2 + y**2 <= 1:
        return 10
    elif x**2 + y**2 <= 25:
        return 5
    elif x**2 + y**2 <= 100:
        return 1
    else:
        return 0

print(score(0,0))
print(score(0,1))
print(score(1,2))
print(score(0.5, -4))