#brute force method for this prblm

arr = [2,3,4,2,4,2,2,4,4,4,4]
major = len(arr)//2
for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            cnt += 1
    if cnt > major:
        print("The majority element is :",arr[i])
        break


        