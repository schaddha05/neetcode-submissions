class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in lastIndex:
                lastIndex[s[i]] = i
        
        start = 0 
        end = 0 
        res = []
        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])
            if i == end: 
                res.append(end - start + 1)
                start = end + 1

        return res