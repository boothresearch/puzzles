def score(x, y):
    radius = (x**2+y**2)**(1/2)
    if radius<=1:
        return(10)
    elif radius<=5:
        return(5)
    elif radius<=10:
        return(1)
    else:
        return(0)
