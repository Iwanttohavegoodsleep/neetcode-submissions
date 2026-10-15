class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int) 
        for num in nums:
            mp[num] += 1

        ret = list(sorted(mp, key = mp.get))

        return ret[len(ret) - k : len(ret)]

            
        


        