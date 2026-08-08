class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tFreq = {} # character -> frequency in t 
        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1 

        window = {} 
        left = 0
        right = 0 
        length = float('inf')
        l = 0
        have = 0 

        for r in range(len(s)):
            if s[r] in tFreq:
                window[s[r]] = window.get(s[r], 0) + 1 
            
            if s[r] in tFreq and window[s[r]] == tFreq[s[r]]:
                have += 1

            while have == len(tFreq):
                if r - l + 1 < length:
                    length = r - l + 1 
                    left = l 
                    right = r 

                if s[l] in tFreq:
                    window[s[l]] -= 1

                if s[l] in tFreq and window[s[l]] < tFreq[s[l]]:
                    have -= 1

                if s[l] in tFreq and window[s[l]] == 0:
                    del window[s[l]]

                l += 1

            
            
        
        return "" if length == float('inf') else s[left:right + 1]



