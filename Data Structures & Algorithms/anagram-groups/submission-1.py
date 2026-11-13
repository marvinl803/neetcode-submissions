from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''

        '''

        dicti = defaultdict(list)

        for string in strs:
            sorted_str = "".join(sorted(string))

            dicti[sorted_str].append(string)

        final_arr = []

        for vals in dicti.values():
            final_arr.append(vals)
        return final_arr


        