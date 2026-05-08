class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0 
        for r in range(len(arr)):
            if r - l + 1 > k:
                l += 1 
            
            if (r-l+1) == k and ((sum(arr[l:r+1]) / (r-l+1)) >= threshold):
                res += 1

        
        return res