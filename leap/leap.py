def leap_year(year):
    if year%4==0:
        if year%400==0:
         print("leap year")
        elif year%100==0:
         print("not leap year")
        else:
            print("leap year")
    print("not leap year")
            
