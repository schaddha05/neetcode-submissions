class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = float('inf')
        lower = 1
        upper = max(piles) 

        while lower <= upper:
            mid = (upper + lower) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/mid)

            if totalTime <= h:
                k = min(mid, k)
                upper = mid - 1
            else:
                lower = mid + 1
        
        return k

