def leap_year(year):
    
    div_4    = (year % 4)   ==0
    div_100  = (year % 100) ==0
    div_400  = (year % 400) ==0
    
    if div_4 and (not div_100 or div_400): 
        print("the year " + str(year) + " is leap")
    else:
        print("the year " + str(year) + " is not leap")

