class Solution:
    from collections import defaultdict
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tFreq = defaultdict(int)
        for c in t:
            tFreq[c] += 1
        
        window = defaultdict(int)
        L = -float('inf')
        R = float('inf')
        length = float('inf')
        l = 0 
        have = 0 
        for r in range(len(s)):
            if s[r] in tFreq:
                window[s[r]] += 1
            
            if s[r] in tFreq and window[s[r]] == tFreq[s[r]]:
                have += 1
            
            while have == len(tFreq): # valid window, update pointers 
                if r - l + 1 < length:
                    length = r - l + 1 
                    L = l 
                    R = r 
                if s[l] in tFreq:
                    window[s[l]] -= 1
                    if window[s[l]] < tFreq[s[l]]:
                        have -= 1
                
                l += 1

            
           

        if length == float('inf'): return ""

        return s[L: R + 1]
