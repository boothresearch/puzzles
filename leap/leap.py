def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return "No"
        else :
            return "YES"
    else :
        return "No"
print(leap_year(1999))
