def leap_year(year):
    
    #Check if year is divisible by 400, then leap
    if year % 400 == 0:
        return(True)
    
    #If not, check if year is divisible by 100, then false
    elif year % 100 == 0:
        return(False)
    
    #If not, check if year is divisible by 4, then true
    elif year % 4 == 0:
        return(True)
    
    #Else, year is not a leap year
    else:
        return(False)


