from string import *
def count_words(sentence):
    sentence = str.lower(sentence)
    current = ""
    dlist = {}
    wlist = []
    for letter in sentence:
        if letter == " ":
            if current in wlist:
                dlist[current] += 1
            else:
                wlist.append(current)
                dlist[current] = 1
            current = ""
        else:
            current = current + letter
    for word in wlist:
        print(word + ": " + str(dlist[word]))




    
