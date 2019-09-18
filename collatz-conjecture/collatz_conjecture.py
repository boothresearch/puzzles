def steps(number):
    i=0
    while True:
        if number == 1:
            return i
        if number % 2 == 0:
            number = number/2
        else:
            number = 3*number+1
        i=i+1
