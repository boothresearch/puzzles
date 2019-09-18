def steps(number):
    n = number
    step = 1
    while n !=1:
        print(step, n)
        if n % 2 == 0:
            n = n/2        
        else:
            n = 3 * n+1
        step +=1
    print(step, n)
    return step

