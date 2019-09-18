import re

def count_words(sentence):
    ## Set possible regex patterns
    #number_ptrn = r'(\d+)(\W)*((\s|\t|\n)|$)'
    word_ptrn = r'([a-zA-Z0-9]+(\'+[a-zA-Z0-9]+)?)((\s|\t|\n|\W|_)|$)'
    ptrn_list = [word_ptrn]
    
    # Get a list of all words, numbers and contractions
    # separated by some type of white space
    
    word_list = list()
    matches = dict()
    for ptrn in ptrn_list:
    
        matches[ptrn] = re.findall(ptrn,sentence.lower())
    
        for match in matches[ptrn]:
            word_list.append(match[0])

            
    # Get a list of unique word occurences and 
    # an empty dictionary to store counts in
    word_list_uniques = set(word_list)
    count_dict = dict()
    for str in word_list_uniques:
        count_dict[str] = word_list.count(str)
        
        
    return count_dict
    



example_phrase = "This is an EXAMPLE phrase that contains 1 example ! what about this111223 3"

print(count_words(example_phrase))


