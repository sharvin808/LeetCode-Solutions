class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        cons = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cons += 1
                if cons > maxi:
                    maxi = cons
            else:
                cons = 0
        return maxi
        