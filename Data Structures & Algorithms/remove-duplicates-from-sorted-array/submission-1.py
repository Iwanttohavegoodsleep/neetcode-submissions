class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        pos = 0

        for x in range(0, len(nums)):
            if nums[pos] != nums[x]:
                pos = pos + 1
                nums[pos] = nums[x]
            else: 
                continue

        return pos+1
 
            
            