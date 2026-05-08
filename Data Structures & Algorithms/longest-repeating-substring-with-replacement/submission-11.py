class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0 
        unique = {}
        left = 0 
        mostPopular = 0 
        for right in range(len(s)):
            unique[s[right]] = unique.get(s[right],0) + 1
            mostPopular = max(unique.values())
            while (right-left + 1) - mostPopular > k:
                unique[s[left]] -=1
                if unique[s[left]] <= 0:
                    del unique[s[left]]
                left+=1
            maxLength = max(maxLength, right-left + 1)
            
        return maxLength

