arr = [1,1,2,2,3,4,4]
xor = 0
for i in range(len(arr)):
    xor = xor ^ arr[i]
print(xor)