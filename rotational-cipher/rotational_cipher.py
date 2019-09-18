def rotate(text, key):
    cipher = ""
    for i in range(0,len(text)):
        
        if 65 <= ord(text[i]) <= 90:
            if ord(text[i])+key > 90:
                cipher = cipher + chr(ord(text[i]) + key - 90 + 64)
                #print(ord(text[i]), ord(text[i]) + key)
            else:
                cipher = cipher + chr(ord(text[i])+key)
                #print(ord(text[i]), ord(text[i]) + key)
        else:
            if 97 <= ord(text[i]) <= 122:
                if ord(text[i])+key > 122:
                    cipher = cipher + chr(ord(text[i]) + key - 122 + 96)
                else:
                    cipher = cipher + chr(ord(text[i])+key)
                
            else:
                cipher = cipher + text[i]
    print("ORT"+str(key)+ " " + text + " gives: " + cipher)
    pass
