def score(x, y):
    # calculate Euclidean distance
    d = x**2 + y**2
    
    #defining scores
    if (d > 100):
        score=0
    
    elif (d<=100) & (d>25):
        score = 1 
        
    elif (d<= 25) & (d>1):
        score =5
        
    elif (d <=1):
        score =10 

    #return function
    return(score)

#print(score(30,2))