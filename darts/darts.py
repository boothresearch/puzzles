def score(x, y):
    if x**2 + y**2 <= 1:
        return(10)
    elif x**2 + y**2 <= 25:
        return(5)
    elif x**2 + y**2 <= 100:
        return(1)
    else:
         return(0)

