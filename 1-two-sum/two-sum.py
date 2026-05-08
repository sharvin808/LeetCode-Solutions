class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        seen = {}
        for i,nums in enumerate(num):
            complement = target - nums
            if complement in seen:
                return(seen[complement],i)
            seen[nums] = i

