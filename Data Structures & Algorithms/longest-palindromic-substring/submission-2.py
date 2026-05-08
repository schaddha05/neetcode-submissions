class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0] 
        longest = 1
        for i in range(len(s)):
            # odd length 
            l = i -1 
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l: r + 1]) > longest:
                    longest = len(s[l: r + 1])
                    ans = s[l: r + 1]
                l -= 1 
                r += 1
            
            # even length 
            l = i 
            r = i+1
            while r < len(s) and l>=0 and s[l] == s[r]:
                if len(s[l: r + 1]) > longest:
                    longest = len(s[l: r + 1])
                    ans = s[l: r + 1]
                l -= 1 
                r += 1

        return ans

