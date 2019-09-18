def steps(number):
    if number <= 0:
        raise ValueError('Input must be strictly positive!')
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
            steps += 1
        else:
            number = (3 * number) + 1
            steps += 1
    return steps