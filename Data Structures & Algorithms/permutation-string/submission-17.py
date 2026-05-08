class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        for c in s1:
            count1[c] += 1

        window = defaultdict(int) 
        l = 0 
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                if window == count1:
                    return True 
                window[s2[l]] -= 1
                if not window[s2[l]]:
                    del window[s2[l]]
                l += 1

            window[s2[r]] += 1
            if window == count1:
                return True 
                
        return False 