class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i, num in enumerate(nums):
            diff = target - num 
            if num in dp:
                return [dp[num], i]
            else:
                dp[diff] = i


        return [0, 0] 
        