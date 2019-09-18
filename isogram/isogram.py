def is_isogram(word):
    if isinstance(word,str):
        w = word.lower() # assuming you want a case in-sensitive search
        return word, len(w) == len(set(w)) if w else False
    else:
        raise TypeError('Argument should be a string')
            
