def leap_year(year):

    print(year)
    temp1 = (year % 4)
    temp2 = temp1 + (year % 100) 
    temp3 = temp2 + (year % 400)
    
    if (temp1 == 0) and (temp2 == 1 or temp3 == 0):
        x = True
    else:
        x = False
    
    print (x)
    return x

leap_year(1900)
leap_year(1901)
leap_year(2000)
leap_year(2001)
