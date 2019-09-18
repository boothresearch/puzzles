def score(x, y):
    r=10
    xc=0
    yc=0
    ro=5
    rt=1
    
    if (x-xc)**2+(y-yc)**2 > r**2:
   
        score= 0
    elif (x-xc)**2+(y-yc)**2 >ro**2:
        score= 1
        
    elif (x-xc)**2+(y-yc)**2 >rt**2:
        score= 5
    elif    (x-xc)**2+(y-yc)**2<=rt**2:
        score= 10
    return score
        
print(score(2,2))