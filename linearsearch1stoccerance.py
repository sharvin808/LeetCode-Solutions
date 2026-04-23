arr = [1,2,3,4,5,6,7,4,3]
target = 4
flag = 0
for i in range(len(arr)):
    if arr[i] == 4:
        flag = 1
        print("First occurence is at",i)
        break
if flag == 1:
    print("Target found successfully")
else:
    print("Target doesn't found")