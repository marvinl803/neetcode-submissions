from collections import defaultdict 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dicti = defaultdict(int)

        for c in s:
            dicti[c] += 1

        for c in t:
            if c not in dicti:
                return False
            dicti[c] -= 1
        
        for value in dicti.values():
            if value != 0:
                return False
        return True
        
        
        