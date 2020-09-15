def count_words(sentence):
    word_count_dict = {}
    word_list = sentence.split()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
    
