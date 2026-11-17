class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        [2,20,4,10,3,4,5]
         i    j

        '''

        num_set = set(nums)
        longest = 0

        for n in num_set:
            # if n is NOT the start of a sequence, skip it
            if n - 1 in num_set:
                continue
            # otherwise, count how long the sequence goes from n
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)

        return longest