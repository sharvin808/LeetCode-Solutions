arr = [1,2,3,4,5,6,7,4,3]
target = 4
for i in range(len(arr)):
    if arr[i] == 4:
        print("First occurence is at",i)
        break
    