def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return not (set(alphabet) - set(phrase))

print(is_pangram("The quick brown fox jumps over the lazy dog"))
