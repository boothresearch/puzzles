def find_anagrams(word, candidates):
    word = list(word)
    for candidate in candidates: 
        candiate = list(candidate)
        if sorted(word) == sorted(candidate):
            print (candidate)
        
