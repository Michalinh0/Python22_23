def first(lines):
    firstletters = [line[0] for line in lines]
    res = ('').join(firstletters)
    return res

def last(lines):
    lastletters = [line[len(line)-1] for line in lines]
    res = ('').join(lastletters)
    return res

line = "abc\ndef ghi        esf\nlsdwer     sad"

lines = line.splitlines()

print(first(lines))
print(last(lines))