
def steps(number):
    
    n_steps = 0
    
    if number <= 0:
        return "Only strictly positive integers allowed!"
    elif number == 1:
        return n_steps
    else:
        while (number != 1):
            if number % 2 == 0:
                number = number / 2
                n_steps += 1
            else:
                number = 3*number + 1
                n_steps += 1
    return n_steps