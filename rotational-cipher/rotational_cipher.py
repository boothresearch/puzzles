def rotate(text, key):
    shifted_text = ''
    for c in text:
        if c == ' ':
            shifted_text += c
        elif 97<=ord(c):
            shifted_text += chr(97 + ((ord(c)-97 + key)%26))
        else: 
            shifted_text += chr(65 + ((ord(c)-65 + key)%26))
            
    return shifted_text

