def count_words(sentence):
    word_count_dict = {}
    word_final_list = []
    word_list = sentence.lower().split()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    print(word_list)
    for item in word_list:
        print(item)
        item_list = []
        for i in range(len(item)):
            if item[i] in alphabet or item[i] in number:
                item_list.append(item[i])
            elif 0<i<len(item)-1:
                if item[i-1] in alphabet and item[i+1] in alphabet:
                    item_list.append(item[i])
        print(item_list)
        word_final_list.append(''.join(item_list))
    for item in word_final_list:
        if item not in word_count_dict:
            word_count_dict[item] = 1
        else:
            word_count_dict[item] += 1
    return word_count_dict

result_dict = count_words("That's the password: 'PASSWORD 123'!\", cried the Special Agent.\nSo I fled.")
print(result_dict)
    
