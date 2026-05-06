arr = [1,4,2,5]
for i in range(len(arr)):
    if arr[i+1] < arr[i]:
        arr[i+1] = arr[i]
    