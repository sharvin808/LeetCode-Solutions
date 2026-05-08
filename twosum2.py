#better solution for two sum using hashing method
arr = [2,6,5,8,11]
target = 14
seen = {}
for i,num in enumerate(arr):
    complement = target - num
    if complement in seen:
        print("The two sum is at:",seen[complement],i)
    seen[num] = i
