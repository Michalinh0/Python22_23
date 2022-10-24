
def sort_by_alphabet(words):
    words = sorted(words)
    return words

def sort_by_length(words):
    words = sorted(words , key = len)
    return words

line = "ac\ndeasf ghis        esfcsde\nlsdwer     sad"
words = line.split()
print(sort_by_alphabet(words))
print(sort_by_length(words))
