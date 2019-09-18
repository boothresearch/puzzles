def is_isogram(string):
    string = string.lower()
    letter_list = []
    for letter in string:
        if letter in letter_list:
            return False    
        letter_list.append(letter)
    return True    
