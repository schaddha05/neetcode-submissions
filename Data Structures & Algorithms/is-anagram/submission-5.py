class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for i in range(len(s)):
            chars[s[i]] = chars.get(s[i],0) + 1
        
        for char in t:
            if char in chars:
                chars[char]-=1
    
        for key in chars:
            if chars[key] != 0:
                return False
        return True 