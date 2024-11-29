'''
def removeChar(s,c):
     return s.replace(c,'')


def removeChar(s,c):
    return ''.join([x for x in s if x != c])




'''

def removeChar(s,c):
    newStr = ''
    for i in s:
        if i != c:
            newStr += i
    return newStr

print(removeChar('hello','l'))
