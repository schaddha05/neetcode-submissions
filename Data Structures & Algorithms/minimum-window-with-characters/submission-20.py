class Solution:
    from collections import defaultdict
    import math
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tFreq = defaultdict(int)
        for c in t:
            tFreq[c] += 1
        
        window = defaultdict(int)
        l = 0 
        have = 0
        start = 0 
        end = 0 
        length = math.inf
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in tFreq and window[s[r]] == tFreq[s[r]]:
                have += 1
            while have == len(tFreq):
                if r - l + 1 < length:
                    length = r - l + 1
                    start = l
                    end = r

                window[s[l]] -= 1
                if s[l] in tFreq and window[s[l]] < tFreq[s[l]]:
                    have -= 1
              
                l += 1


        return "" if length == math.inf else s[start:end+1]



