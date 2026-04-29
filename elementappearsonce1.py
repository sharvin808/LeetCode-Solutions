arr = [1,1,2,2,3,4,4]
num = 0
for i in range(len(arr)):
    num = arr[i]
    cnt = 0
    for j in range(len(arr)):
        if num == arr[j]:
            cnt += 1
    if cnt == 1:
        print(num)