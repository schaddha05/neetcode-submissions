class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s) 

        for i in range(len(s)):
            # odd length 
            l = i -1 
            r = i + 1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                res += 1
                l -= 1 
                r += 1
            
            # even length
            l = i 
            r = i + 1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                res += 1
                l -= 1 
                r += 1
        return res
