class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r 

        while l <= r:
            mid = (r+l)// 2

            totalTime = 0 
            for p in piles:
                totalTime += math.ceil(p/mid)
            
            if totalTime <= h:
                k = mid 
                r = mid - 1 
            else: 
                l = mid + 1

        return k
