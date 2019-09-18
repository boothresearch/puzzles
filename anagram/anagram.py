def find_anagrams(word, candidates):
    list = []
    for i in candidates:
        if ''.join(sorted(i)).lower()==''.join(sorted(word)).lower():
            list.append(i)
    print(list)
