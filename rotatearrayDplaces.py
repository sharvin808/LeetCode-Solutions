arr = [1,2,3,4,5,6]
left = 0
d = 13
while left < d:
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    left += 1
print(arr)