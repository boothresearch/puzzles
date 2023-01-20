counter = 0
def steps(number, counter = 0):
    if number < 1:
        raise ValueError('number should be positive')
    elif number % 2 == 0:
        number = number / 2
        counter += 1
        return steps(number, counter)
    elif number == 1:
        return counter
    else:
        number = 3*number + 1
        counter += 1
        return steps(number, counter)
