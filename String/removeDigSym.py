# function to remove characters except alphabets from a string.

def removeDigSym(s):
    return ''.join(e for e in s if e.isalpha())

