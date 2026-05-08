class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s.lower()
        if len(s) == 0:
            return 0 
        
        maxLength = 1
        left = 0 
        seen = []
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.append(s[right])
            maxLength = max(maxLength, len(seen))
        return maxLength
        
