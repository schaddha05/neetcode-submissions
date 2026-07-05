class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1Freq = [0 for _ in range(26)]
        for s in s1:
            s1Freq[ord(s) - ord('a')] += 1

        window = [0 for _ in range(26)]
        
        l = 0 
        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == k:
                if window == s1Freq:
                    return True 

                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
                
        return False
