def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(leap_year(1999))
    #pass
# ctrl-j 
# cd leap
# python3 leap.py
# python3 -i leap.py
# 



## My Exercise
# exit() or quit()
# q to return