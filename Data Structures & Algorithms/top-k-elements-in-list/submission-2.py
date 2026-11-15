from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dicti = defaultdict(int)
        
        for num in nums:
            dicti[num] += 1
        
        dicti = dict(sorted(dicti.items(), key=lambda x: x[1], reverse=True))

        return list(dicti)[:k]