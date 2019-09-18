def is_pangram(sentence):
    str(sentence)
    alphabet = 'abcdefghijklmnopqrstuvwqxz'
    for letter in alphabet:
        if letter not in sentence.lower():
            return False 
    return True 


