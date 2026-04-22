arr = [1,1,2,2,2,3,3]
i = 0
for j in range(1,len(arr)):
    if arr[j] != arr[i]:
        i += 1
        arr[i] = arr[j]
for k in range(i+1,len(arr)):
    arr[k] = '_'
print(arr)
