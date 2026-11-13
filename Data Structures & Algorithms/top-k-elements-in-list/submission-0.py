from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dicti = defaultdict(int)

        for num in nums:
            dicti[num] += 1

        sorted_dicti = dict(sorted(dicti.items(), key=lambda item: item[1], reverse=True))

        most_frequent = k
        ans = []
        for key, val in sorted_dicti.items():
            ans.append(key)
        return ans[:k]





        