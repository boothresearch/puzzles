def is_isogram(string):
    for i in range(len(string)):
        if i == 0:
            letters = [string[i]]
        else:
            if string[i] == " " or string[i] == "-":
                pass
            elif string[i] in letters:
                return(string + " is not an isogram")
            else:
                letters.append(string[i])
    return(string + " is an isogram")
