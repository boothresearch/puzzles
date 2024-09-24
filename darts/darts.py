import math
def score(x, y):
    # Calculate the distance of the dart from the center (0, 0)
    distance = math.sqrt(x**2 + y**2)
    
    # Determine the score based on the distance
    if distance > 10:
        return 0  # Outside the target
    elif distance > 5:
        return 1  # Outer circle
    elif distance > 1:
        return 5  # Middle circle
    else:
        return 10  # Inner circle


    pass
