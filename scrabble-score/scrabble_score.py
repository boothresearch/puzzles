def score(word):
    Dict = {'A':1,'a':1, 'e':1,'E':1,'I':1,'i':1,'O':1,'o':1,'t':1,'d':2,'g':2,
            'U':1,'u':1,'L':1,'l':1,'N':1,'n':1,'R':1,'r':1,'S':1,'s':1,'T':1,'D':2,'G':2,
          'B':3,'C':3,'M':3,'P':3, 'F':4,'H':4,'V':4,'W':4,'Y':4, 'K':5, 'J':8,'X':8,'Q':10,'Z':10,
           'b':3,'c':3,'m':3,'p':3, 'f':4,'h':4,'v':4,'w':4,'y':4, 'k':5, 'j':8,'x':8,'q':10,'z':10}
    
    count = 0
    for i in range(0, len(word)):
        if word[i].isalpha():
            count += int(Dict.get(word[i]))
    return count
