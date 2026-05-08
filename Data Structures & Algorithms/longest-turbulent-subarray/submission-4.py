class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        maxLen = 1
        curLen = 1
        prevSign = 0

        for i in range(1, len(arr)):
            c = (arr[i] > arr[i-1]) - (arr[i] < arr[i-1])

            if c == 0:
                curLen = 1
            elif prevSign * c == -1:
                curLen += 1
            else:
                curLen = 2
            
            prevSign = c 
            maxLen = max(curLen, maxLen)
        
        return maxLen