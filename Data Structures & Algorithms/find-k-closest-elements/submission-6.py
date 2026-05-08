class Solution:
    import heapq
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0 
        r = len(arr) - k

        while l < r:
            m = (r+l) // 2
            if abs(x - arr[m]) > abs(arr[m+k] - x):
                l = m + 1 
            else:
                r = m
        
        return arr[l:l+k]


        
    



