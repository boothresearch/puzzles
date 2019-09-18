def leap_year(year):
<<<<<<< HEAD
    return("Party like it's " + str(year))

print(leap_year(1999))
=======
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               print("{0} is a leap year".format(year))
           else:
               print("{0} is not a leap year".format(year))
       else:
           print("{0} is a leap year".format(year))
    else:
       print("{0} is not a leap year".format(year))

>>>>>>> d6aba258212e553d732989a33568975fc7ec5e6d
