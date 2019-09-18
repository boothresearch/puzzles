def score(word):
    word = word.lower()
    group1 = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
    group2 = ['d', 'g']
    group3 = ['b', 'c', 'm', 'p']
    group4 = ['f', 'h', 'v', 'w', 'y']
    group5 = ['k']
    group8 = ['j', 'x']
    group10 = ['q', 'z']
    score = 0
    for letter in word:
        if letter in group1:
            score += 1
        elif letter in group2:
            score += 2
        elif letter in group3:
            score += 3
        elif letter in group4:
            score += 4
        elif letter in group5:
            score += 5
        elif letter in group8:
            score += 8
        elif letter in group10:
            score += 10
    return score
