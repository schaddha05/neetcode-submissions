class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        tFreq = {}
        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1 
        
        minLeft = float('inf')
        minRight = float('inf')

        have = 0 # += 1 when window[char in t] == tFreq[char in t] 
        length = float('inf') # length of cur smallest window
        l = 0 
        window = {}

        for r in range(len(s)):
            if s[r] in tFreq:
                window[s[r]] = window.get(s[r], 0) + 1 
            
            if s[r] in tFreq and window[s[r]] == tFreq[s[r]]:
                have += 1
            
            while have == len(set(t)):
                if r - l + 1 < length:
                    minLeft = l
                    minRight = r 
                    length = r - l + 1
                
                if s[l] in tFreq:
                    window[s[l]] -=1 
                
                if s[l] in tFreq and window[s[l]] < tFreq[s[l]]:
                    have -= 1
                l += 1

        return "" if length == float('inf') else s[minLeft: minRight + 1]    
                

            




