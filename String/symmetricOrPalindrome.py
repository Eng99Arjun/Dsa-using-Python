def isPalindrome(s):
    return s == s[::-1]

def isSymmetric(s):
    half = len(s) // 2
    first = s[:half]
    second = s[half:] if len(s)%2 ==0 else s[half+1:]
    return first == second


str1 = input("Enter a string: ")

if isPalindrome(str1):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

if isSymmetric(str1):
    print("The string is symmetric.")
else:
    print("The string is not symmetric.")   
