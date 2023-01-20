def is_pangram(sentence):
    """
    To see if all 26 alphabets are being used
    """

    # to lower
    sentence = sentence.lower()

    # create a hashmap to store the frequency of each ascii letter
    # frequency = dict()
    frequency = [0]*26
    # a: 97; z:122
    for char in sentence:
        if ord(char)<97 or ord(char)>122:
            pass
        else:
            frequency[ord(char) - 97] += 1

    for i in frequency:
        if i == 0:
            return False
        
    return True
    
