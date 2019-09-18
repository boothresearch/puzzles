def score(x, y):
    dis = (x*x+y*y)**0.5;
    if dis<=10 and dis>5:
        score = 1
    elif dis<=5 and dis>1:
        score = 5
    elif dis <=1: 
        score = 10
    else:
        score = 0
    print(score)
        
