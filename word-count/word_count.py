def count_words(sentence):
    import re
    word_dic = {}
    word_list = re.findall(r"[0-9A-Za-z']+", sentence)
    print(word_list)
    for word in word_list:
        word = word.lower().strip("'")
        if word not in word_dic:
            word_dic[word] = 1
        else:
            word_dic[word] += 1

    return word_dic
