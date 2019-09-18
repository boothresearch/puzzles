x = int(input('Please enter the x coordinate:'))
y = int(input('Please enter the y coordinate:'))
def score(x, y):
    if x**2+y**2>100:
        return 0 
    elif x**2+y**2<=100 and x**2+y**2>25:
        return 1 
    elif x**2+y**2<=25 and x**2+y**2>1:
        return 5 
    elif x**2+y**2>=0 and x**2+y**2<=1:
        return 10 
    else:
        print("Error")
print("The score is: ", score(x,y))