# program to count number of vowels, consonants and spaces.

def countChar(s):
    vowels = 0
    consonants = 0
    spaces = 0
    for i in s:
        if i==' ':
            spaces += 1
        elif i in 'aeiouAEIOU':
            vowels += 1
        else:
            consonants += 1
    return vowels,consonants,spaces

print(countChar('hello world')) # (3, 7, 1)