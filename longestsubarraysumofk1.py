#brute force method for finding longest subarray with sum of k
arr = [1,2,3,1,1,1,1,4,2,3]
target = 3
length = 0 
for i in range(len(arr)):
    for j in range(i,len(arr)):
        s = 0
        for k in range(i,j+1):
            s += arr[k]
        if s == target:
            length = max(length,j-i+1)
print(length)
