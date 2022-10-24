line = "abc\ndef ghi        esf\nlsdwer     sad"

words = line.split()

print(words)

print(sum(len(x) for x in words))