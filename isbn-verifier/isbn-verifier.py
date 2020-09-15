def check(isbn):
    isbn = isbn.replace("-","").replace(" ", "")
    check_digit = int(isbn[-1])
    match = re.search(r'(\d{9})$', isbn[:-1])

    if not match:
        return False

    digits = match.group(1)
    result = 0
    for i, digit in enumerate(isbn):
        result += (i+1)*int(digit)
    return True if (result % 11) == check_digit else False
