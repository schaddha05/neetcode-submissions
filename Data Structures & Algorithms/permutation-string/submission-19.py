class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1Freq = defaultdict(int)
        window = defaultdict(int)
        for s in s1:
            s1Freq[s] += 1
        
        l = 0 
        for r in range(len(s2)):
            window[s2[r]] += 1
            if r - l + 1 == k:
                if window == s1Freq:
                    return True 
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
        return False
