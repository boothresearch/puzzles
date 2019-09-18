def rotate(text, key):
    ciphertext=''
    for ch in text: 
        if ch.isalpha():
            i = ord(ch) + key 
            if i>ord('z'):
                i-=26
            finalletter=chr(i)
            ciphertext+=finalletter
    return ciphertext


