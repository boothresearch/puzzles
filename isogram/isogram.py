def is_isogram(string):
    
    try:
        original_string = string # Saving the original string 
        
        # The idea is to count the occurrences of each letter in the string
        # If one of the occurrences is greater than 1, the word is NOT an isogram
        # Otherwise, it is an isogram
        
        last_value = 1
        string = string.replace(" ", "")
        string = string.replace("-", "")
        
        while last_value == 1 and len(string) > 0:
            first_character = string[0]
            last_value = string.count(first_character)
            string = string.replace(first_character, "")
    
        if last_value == 1:
            return "The string \" " + original_string + " \" is an isogram!" 
        
        else:
            return "The string \"" + original_string + "\" is NOT an isogram because the letter \"" + first_character + "\" appears " + str(last_value) + " times!"
            
    
    except:
        print("The input should be a String!!!")
        print("\n Please, insert your input between quotes, e.g. \" string \" ")
    