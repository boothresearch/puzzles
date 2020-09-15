def find_anagrams(word, candidates):
    cand_list = []
    word_set = set(word)
    for cand in candidates:
        cand_set = set(cand)
        if cand_set==word_set and len(word)==len(cand):
            cand_list.append(cand)
    
    return cand_list

print(find_anagrams('listen',["enlists","google","inlets","banana"]))
