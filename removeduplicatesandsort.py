arr = [1,1,2,2,2,3,3]
i = 0
j = 1
for j in range(len(arr)):
    if arr[j] != arr[i]:
        arr[i+1] = arr[j]
        i += 1
print(arr[:i+1])
        