def score(word):

    word = word.upper() # converting everything to uppercase
    letters = [x for x in word] # getting a list of characters in the word
    total_points = 0 # the variable to contain the points

    point_dict = {1:["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2:["D", "G"], 3:["B", "C", "M", "P"], 4:["F", "H", "V", "W", "Y"], 
    5:["K"], 8:["J", "X"], 10:["Q", "Z"]} # dictionary of points

    for char in letters: # looping across the characters
        for key in point_dict.keys(): # looping across dictionary keys
            if char in point_dict[key]:
                total_points = total_points + key
    
    return total_points

    