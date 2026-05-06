#optimal solution for longest subarray with sum of k;
#better solution is using hashing, i don't get it;
arr = [1,2,3,1,1,1,1,4,2,3]
sum = arr[0]
left,right = 0,0
target = 3
length = 0
while(right < len(arr)):
    while(left <= right and sum > target):
        sum -= arr[left]
        left += 1
    if sum == target:
        length = max(length,right-left+1)
    right += 1
    if right < len(arr):
        sum += arr[right]
print(length)