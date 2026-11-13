class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        sum of 2 integers equals target target = 7
        [3,4,5,6,7]
         |

        dicti: 
        
        '''

        dicti = dict()

        for i in range (len(nums)):
            diff = target - nums[i]

            if nums[i] in dicti:
                return [dicti[nums[i]], i]
            else:
                dicti[diff] = i
        return [-1, -1]