# def removeVowels(s):
#     str1=''
#     for char in s:
#         if char not in 'aeiou':
#             str1+=char
#     return str1

# print(removeVowels('hello')) # hll

def removeVowels(s):
    return ''.join([char for char in s if char not in 'aeiou'])
