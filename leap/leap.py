def leap_year(year):
    if year % 400 == 0:
        return(str(year) + " is a leap year")
    elif year % 100 == 0:
        return(str(year) + " is not a leap year")
    elif year % 4 == 0:
        return(str(year) + " is a leap year")
    else:
        return(str(year) + " is not a leap year")


