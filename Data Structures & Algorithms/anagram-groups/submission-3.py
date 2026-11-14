from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''

        '''

        dicti = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for c in string:
                count[ord(c) - ord('a')] += 1
            dicti[tuple(count)].append(string)
        return list(dicti.values())


