class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        seq = set(nums)
        print(seq)

        for num in nums:
            if num - 1 in seq:
                continue
            
            curr_len = 0
            while num + curr_len in seq:
                curr_len += 1
                length = max(length, curr_len)
        return length
        