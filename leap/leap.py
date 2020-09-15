def leap_year(year):

    print(year)
    temp1 = (year % 4)
    temp2 = temp1 + (year % 100) 
    temp3 = temp2 + (year % 400)
    if (temp1 == 0) and (temp2 >= 1 or temp3 == 0):
        x = True
    else:
        x = False
    return x
