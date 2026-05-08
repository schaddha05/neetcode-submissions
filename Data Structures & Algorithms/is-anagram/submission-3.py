class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars_s = {}
        chars_t = {}
        for i in range(len(s)):
            chars_s[s[i]] = chars_s.get(s[i],0) + 1
            chars_t[t[i]] = chars_t.get(t[i],0) + 1

    
        return chars_s == chars_t