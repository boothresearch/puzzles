def leap_year(year):
    if not isinstance(year,int):
        raise TypeError("Year entered must be an integer!")
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True

year = input("Please choose the year:")
try:
    year = int(year)
except TypeError:
    print("Please input an integer!")

print(leap_year(year))
