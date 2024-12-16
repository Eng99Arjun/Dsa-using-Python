# program to get sum of digits of a string

def stringDigSum(s):
    return sum(int(e) for e in s if e.isdigit())

print(stringDigSum('abc123')) # 6