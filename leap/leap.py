def leap_year(year):
    if (year%4 == 0) & (year%100 != 0):
        return True
    elif (year%400 == 0):
        return True
    else:
        return False

#print(leap_year(1999))
