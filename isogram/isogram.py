def is_isogram(string):
    string = string.lower()
    sofar = ""
    for char in string:
        if char.isalpha():
            if char in sofar:
                return False
            sofar = sofar + char
    return True
            
            
