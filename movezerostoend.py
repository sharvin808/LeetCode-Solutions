arr = [1,0,2,3,2,0,0,4,5,1]
z = -1
for i in range(len(arr)):
    if arr[i] == 0:
        z = i
        break
for j in range(z+1,len(arr)):
    if arr[j] != 0:
        arr[z],arr[j] = arr[j],arr[z]
        z += 1
print(arr)