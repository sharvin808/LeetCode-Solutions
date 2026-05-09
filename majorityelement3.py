#optimal soln for this using Moore's Voting Algorithm

nums = [2,3,4,5,2,2,2,2,3,2,2]
cnt = 0
major = len(nums) // 2
for i in range(len(nums)):
    if cnt == 0:
        cnt = 1
        el = nums[i]
    elif nums[i] == el:
        cnt += 1
    else:
        cnt -= 1
cnt1 = 0
for i in range(len(nums)):
    if nums[i] == el:
        cnt1 += 1
if cnt1 > major:
    print("The majority element is:",el)