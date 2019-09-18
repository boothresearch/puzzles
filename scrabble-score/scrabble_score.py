from string import *
def score(word):
    word = str.lower(word)
    points = 0
    for letter in word:
        if letter in ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]:
            points += 1
        elif letter in ["d", "g"]:
            points += 2
        elif letter in ["b", "c", "m", "p"]:
            points += 3
        elif letter in ["f", "h", "v", "w", "y"]:
            points += 4
        elif letter in ["k"]:
            points += 5
        elif letter in ["j", "x"]:
            points += 8
        elif letter in ["q", "z"]:
            points += 10
    return(word + " is worth " + str(points) + " points :)") 
