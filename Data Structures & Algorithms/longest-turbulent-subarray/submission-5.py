class Solution:
    
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1 

        def sign(x, y):
            if x < y: 
                return -1 
            if x > y:
                return 1
            return 0 

        res = 1 
        l = 0 
        for r in range(1, len(arr)):
            curSign = sign(arr[r-1], arr[r])
            if curSign == 0:
                l = r
            elif r > 1 and curSign == sign(arr[r-2], arr[r-1]):
                l = r - 1
            
            res = max(res, r - l + 1)
        
        return res



