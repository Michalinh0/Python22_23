line = "abc\ndef ghi        esf\nlsdwer     sad"

words = line.split()

words.sort(key = len , reverse = True)

print(words[0])

print(len(words[0]))