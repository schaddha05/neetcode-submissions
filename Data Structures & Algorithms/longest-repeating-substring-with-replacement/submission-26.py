class Solution:
    from collections import defaultdict 
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = 1
        l = 0
        mostPop = 0
        for r in range(len(s)):
            freqs[s[r]] += 1
            mostPop = max(mostPop, freqs[s[r]])
            while (r - l + 1) - mostPop > k:
                freqs[s[l]] -= 1
                if freqs[s[l]] == 0:
                    del freqs[s[l]]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
            
