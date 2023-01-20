def steps(number):
    counter=0
    if number<=0 or number % 1 != 0:
        raise ValueError("number must be a positive integer") 
    else:
        while number!=1:
            if number % 2 == 0:
                number = number/2
            else:
                number = 3*number+1
            counter+=1
        return(counter)
