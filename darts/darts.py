import math

def score(x, y):
    d=math.sqrt(x*x + y*y)
    if d<=10 and d>5:
        return("Your score is 1")
    elif d<=5 and d>1:
        return("Your score is 5")
    elif d<=1:
        return("Your score is 10")
    else:
        return("You missed the target")
    
print(score(1, 3))