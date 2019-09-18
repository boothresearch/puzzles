def find_anagrams(word, candidates):
    
    anagram = []
    
    word_letters = []
    
    while len(word_letters)<len(word):
        word = str(word)
        for i in list(word):
            if i not in word_letters:
                word_letters.append(i)
    
    word_letters = sorted(word_letters)
    
    for i in list(candidates):
        
        i_letters= []
        
        while len(i_letters)<len(i):
            i = str(i)
            for j in list(i):
                if j not in i_letters:
                    i_letters.append(j)
        
        i_letters = sorted(i_letters)
        
        done = (i_letters == word_letters)
        
        if done == True:
            
            anagram.append(i)
    
    return anagram