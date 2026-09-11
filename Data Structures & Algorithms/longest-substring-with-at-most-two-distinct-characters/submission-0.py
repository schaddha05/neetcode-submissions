class Solution:
    from collections import defaultdict
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = -float('inf')
        window = defaultdict(int)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            while len(window) > 2:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
            
