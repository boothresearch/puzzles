from collections import Counter 

def is_isogram(string):
    input = string
    # count the number of ocurrence of each element 
    frequency = Counter(input)
    # if no character appear more than once - isogram
    print(str(frequency))
    # if a character appears more than once - and they are not space or hypens - not isogram
    # 
    #   if they are space or hypens - isogram
    #   

is_isogram()    