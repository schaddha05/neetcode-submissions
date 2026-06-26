import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 
        high = max(piles)

        k = high

        while low <= high:
            m = (high + low) // 2 

            # verify if we can finish all bananas with rate m 
            curTime = 0 
            for pile in piles:
                curTime += math.ceil(pile/m)
            
            if curTime <= h:
                k = m 
                high = m - 1
            else:
                low = m + 1
        
        return k 
