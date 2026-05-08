class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1 

        result = right
        while left <=right:
            k = (right + left)//2
            totalTime = 0

            for pile in piles:
                totalTime+= math.ceil(pile/k)
            if totalTime <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result




        

