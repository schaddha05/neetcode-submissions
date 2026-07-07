class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tFreq = {}
        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1 
        
        window = {}
        l = 0 
        have = 0
        start = 0 
        end = 0 
        length = float('inf')
        for r in range(len(s)):
            if s[r] in tFreq:
                window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in tFreq and tFreq[s[r]] == window[s[r]]:
                have += 1
        
            while have == len(tFreq):
                if r - l + 1 < length:
                    length = r - l + 1
                    start = l 
                    end = r
        
                if s[l] in tFreq:
                    window[s[l]] -= 1
                if s[l] in tFreq and window[s[l]] < tFreq[s[l]]:
                    have -= 1

                l += 1
        
        return "" if length == float('inf') else s[start: end + 1]

