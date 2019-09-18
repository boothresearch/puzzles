from string import *
def rotate(text, key):
    cyphertext = ""
    text = str.lower(text)
    for letter in text:
        letterint = ord(letter) - 96
        if letterint > 0 and letterint < 27:
            cyphertext = cyphertext + chr(((letterint + key)%26)+96)
        else:
            cyphertext = cyphertext + letter
    print(cyphertext)
