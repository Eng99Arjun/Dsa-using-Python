def revSentence(str1):
    sen = str1.split()[::-1]
    l=[]
    for i in sen:
        l.append(i)
    return " ".join(l)

print(revSentence(input("Enter String")))