class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_str = ""

        for c in s:
            if c.isalnum():
                clean_str += c.lower()
        
        return clean_str == clean_str[::-1]
