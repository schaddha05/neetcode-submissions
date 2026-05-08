class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_chars = [0] * 26
        for c in s1:
            s1_chars[ord(c) - ord('a')]+=1
        
        left = 0
        window = [0] * 26
        for right in range(len(s2)):
            while right - left + 1 > len(s1):
                window[ord(s2[left])-ord('a')]-=1
                left+=1
            window[ord(s2[right])-ord('a')]+=1
            if window == s1_chars:
                return True
        return False 
            