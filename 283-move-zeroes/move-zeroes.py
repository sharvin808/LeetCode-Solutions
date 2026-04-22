class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                z = i
                break
        if z == -1:
            return
        for j in range(z+1,len(nums)):
            if nums[j] != 0:
                nums[z],nums[j] = nums[j],nums[z]
                z += 1    