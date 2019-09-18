def steps(number):  
    if isinstance(number, int):
        if number > 0:
            pass
        else: 
            raise ValueError('The number should be an integer and greater then 0')
    else:
        raise TypeError('The number should be of type integer')
        
    n = number

    step = 0
    while n !=1:
        if n % 2 == 0:
            n = n/2        
        else:
            n = 3 * n+1
        step +=1
    return step
