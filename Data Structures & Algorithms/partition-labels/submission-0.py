class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for ch in s:
            i = s.rfind(ch)
            lastIndex[ch] = i 
        
        start = 0 
        end = 0 
        res = []
        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])
            if i == end: 
                res.append(end - start + 1)
                start = end + 1

        return res