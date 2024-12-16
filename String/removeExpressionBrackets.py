#remove brackets from an expression

# def removeExpressionBrackets(s):
#     return ''.join(e for e in s if e not in ['(',')'])

# print(removeExpressionBrackets('(a+b)')) # ab

# The function removeExpressionBrackets() removes brackets from an expression.


def removeExpressionBrackets(s):
    str1=''

    for char in s:
        if char not in ['(',')']:
            str1+=char
    return str1

print(removeExpressionBrackets('(a+b)')) # ab