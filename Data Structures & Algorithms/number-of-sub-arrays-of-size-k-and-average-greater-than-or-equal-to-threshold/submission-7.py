class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0 

        windowSum = 0 
        l = 0 
        for r in range(len(arr)):
            windowSum += arr[r]
            if r - l + 1 == k: 
                if windowSum/k >= threshold:
                    res += 1
                windowSum -= arr[l]
                l += 1
      
        return res