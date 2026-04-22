nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
k = k % n
for _ in range(k):
    temp = nums[-1]
    for i in range(n-1,0,-1):
        nums[i] = nums[i-1]
    nums[0] = temp
print(nums)
# this method would exceeds the time limit

n = len(nums)
k = k % n
nums.reverse()
nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:]) #this is the optimal method
        