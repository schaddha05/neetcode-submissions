class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        maxLen = 1
        curLen = 1
        prevSign = None
        if arr[1] - arr[0] > 0:
            curLen += 1
            maxLen += 1
            prevSign = '+'
        elif arr[1] - arr[0] < 0:
            curLen += 1
            maxLen += 1
            prevSign = '-'
        else:
            prevSign = ''

        for i in range(2, len(arr)):
            curSign = ''
            if arr[i] - arr[i-1] > 0:
                curSign = '+'
            elif arr[i] - arr[i-1] < 0:
                curSign = '-'
            else:
                curSign = ''
            
            if curSign == '':
                curLen = 1
            elif curSign != prevSign:
                curLen += 1
            else:
                curLen = 2

            prevSign = curSign
            maxLen = max(maxLen, curLen)
        
        return maxLen