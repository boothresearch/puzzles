def score(x, y):
    if(-1<=x<=1 and -1<=y<=1):
        s = 10
    else:
        if(-5<=x<=5 and -5<=y<=5):
            s = 5
        else:
            if(-10<=x<=10 and -10<=x<=10):
                s = 1
            else:
                s = 0
    print("The socre is: " + str(s))
    pass
