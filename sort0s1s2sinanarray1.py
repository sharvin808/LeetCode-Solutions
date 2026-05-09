#brute force is nothing other than iterating through the array and sort it according to its ascending order.
#better soln for this prblm is:

arr = [0,1,1,0,0,1,0,0,0,2,2,1,2]
cnt0,cnt1,cnt2 = 0,0,0
for i in range(len(arr)):
    if arr[i] == 0:
        cnt0 += 1
    elif arr[i] == 1:
        cnt1 += 1
    else:
        cnt2 += 1
for i in range(0,cnt0):
    arr[i] = 0
for i in range(cnt0,cnt0+cnt1):
    arr[i] = 1
for i in range(cnt0+cnt1,cnt0+cnt1+cnt2):
    arr[i] = 2
print(arr)
