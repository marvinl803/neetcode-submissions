class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # Pass 1: left to right
        left = 1
        for i in range(n):
            ans[i] = left        # what goes here is "everything to the left of i"
            left = left * nums[i]          # update left so it's ready for i + 1

        # Pass 2: right to left
        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * right         # combine what's already in ans[i] with right
            right = right * nums[i]         # update right so it's ready for i - 1

        return ans
                