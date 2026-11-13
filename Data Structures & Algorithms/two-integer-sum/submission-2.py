from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        [3,4,5,6] target = 7
           |

         dictionary = 
         {
          3: 0

         }
        '''

        dicti = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in dicti:
                return [dicti[diff], i]

            dicti[nums[i]] = i

        return [-1, -1]


        