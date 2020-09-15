def abbreviate(words):
    word_list = words.split()
    acronym = ""
    for w in word_list:
        acronym= acronym + w[0]
    acronym = acronym.upper()
    return acronym
    
