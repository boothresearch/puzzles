from collections import Counter 

def is_isogram(string):
    #input = string
    # count the number of ocurrence of each element 
    #frequency = Counter(input)
    #print(type(frequency))
    #print(str(frequency))    
    # if no character appear more than once - isogram


    # if a character appears more than once - and they are not space or hypens - not isogram
    # 
    #   if they are space or hypens - isogram
    #   
    # Convert the word or sentence in lower case letters. 
    clean_string = string.lower() 
  

    # Make an empty list to append unique letters 
    letter_list = [] 
  
    for letter in clean_string: 
  
        # If letter is an alphabet then only check 
        if letter.isalpha(): 
            if letter in letter_list: 
                return False
            letter_list.append(letter) 
  
    return True
