arr = [1,2,3,4,5,6,7,4,3]
target = 4
for i in range(len(arr)-1,0,-1):
    if arr[i] == target:
        print("The last occerance is at",i)
        break
