def find_anagrams(word, candidates):
    list = []
    for i in candidates:
        if ''.join(sorted(i))==''.join(sorted(word)):
            list.append(i)
    print(list)
