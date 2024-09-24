def score(x, y):
    # Calculate the distance from the center (0, 0) to the dart's landing point
    distance = math.sqrt(x**2 + y**2)
    
    # Determine the points based on the distance
    if distance <= 1:
        return 10  # Inner circle
    elif distance <= 5:
        return 5   # Middle circle
    elif distance <= 10:
        return 1   # Outer circle
    else:
        return 0   # Outside the target
