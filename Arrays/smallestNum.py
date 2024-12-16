arr=[2,5,7,1,0,5,7,3,2]
smallest =arr[0]
smallestIdx = 0
for i in arr:
    if i>smallest:
        smallest=i
    smallestIdx=arr.index(smallest)
print(smallest,smallestIdx)    