def steps(number):
    if number <= 0:
        raise ValueError("Please provide a positive integer")
    else:
        step = 0
        if number == 1: 
            return step
        else:
            while number != 1:
                if number % 2 == 0:
                    number  = number / 2
                    step += 1
                else: 
                    number  = 3 * number + 1
                    step += 1
            return step

            
