class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        
        window = {}
        matches = 0 
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1 
            if window[s2[r]] == freq.get(s2[r], 0):
                matches += 1 
            elif window[s2[r]] == freq.get(s2[r], 0) + 1:
                # we just over‑filled this char
                matches -= 1

            if r - l + 1 > len(s1):
                if window[s2[l]] == freq.get(s2[l], 0):
                    matches -= 1
                elif window[s2[l]] == freq.get(s2[l],0) + 1:
                    matches += 1
                window[s2[l]] -= 1
                l += 1 
            
            if matches == len(freq):
                return True 
        
        return False 
            
