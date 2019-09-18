
one_val = {k:1 for k in ["A", "E", "I", "O", "U",
              "L", "N", "R", "S", "T"]}
two_val = {k:2 for k in ["D", "G"]}
three_val = {k:3 for k in ["B", "C", "M", "P"]}
four_val = {k:4 for k in ["F", "H", "V", "W", "Y"]}
eight_val = {k:8 for k in ["J", "X"]}
ten_val = {k:10 for k in ["Q", "Z"]}

alphabet_dict = {**one_val, **two_val, **three_val, 
                **four_val, **eight_val, **ten_val}

alphabet_dict["K"] = 5

def score(word):
    word = word.upper()
    chars = list(word)
    points = [alphabet_dict[letter] for letter in chars]
    return(sum(points))

    
        