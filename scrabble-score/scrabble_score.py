one=["A","E", "I", "O", "U", "L", "N", "R", "S", "T"]
two=["D", "G"]
three=["B", "C", "M", "P"]
four=["F", "H", "V", "W", "Y"]
five=["K"]
six=["J","X"]
seven=["Q", "Z"]
count=0
points=0
theword=list(input("Please input a word: "))

def score(word, count, points):
    for i in word: 
        if i in one:
            points+=1
            count = count + 1
        elif i in two:
            points+=2
            count = count + 1
        elif i in three:
            points+=3
            count = count + 1
        elif i in four:
            points+=4
            count = count + 1
        elif i in five:
            points+=5
            count = count + 1 
        elif i in six:
            points+=6
            count = count + 1 
        elif i in seven:
            points+=7
            count = count + 1 
        else:
            print("Error")
    print("The score is: " +str(points))           

score(theword, count, points)




score = {"a": 1 , "b": 3 , "c": 3 , "d": 2 ,
         "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
         "i": 1 , "j": 8 , "k": 5 , "l": 1 ,
         "m": 3 , "n": 1 , "o": 1 , "p": 3 ,
         "q": 10, "r": 1 , "s": 1 , "t": 1 ,
         "u": 1 , "v": 4 , "w": 4 , "x": 8 ,
         "y": 4 , "z": 10}

def word_score(word):
    total = 0;
    for i in word:
        i = i.lower(); 
        total = total + score[i];
    return total;

your_word = input("Please input a word: ");

print(word_score(your_word))

