def rotate(text, key):
    shifted_text = ''
    for c in text:
        if c == ' ':
            shifted_text += c
        else:
            shifted_text += chr(97 + ((ord(c)-97 + key)%26))
    return shifted_text

