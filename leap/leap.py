#def leap_year1(year):
#    return("YEAH!")
# print(leap_year(1999))



#def leap_year2(year):
#    return(year)


def leap_year(year):
    if year % 100 == 0:
        if year % 400 ==0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False