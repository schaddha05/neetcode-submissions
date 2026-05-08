class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = sum(weights)
        l = 1
        h = s
        res = float('inf')
        while l <= h:
            mid = (h+l) // 2 # candidate capacity 

            i = 0 
            total = 0
            d = days
            while d > 0 and i < len(weights):
                curDayTotal = 0 
                while i < len(weights):
                    if curDayTotal + weights[i] > mid:
                        break 
                    curDayTotal += weights[i] 
                    i += 1

                total += curDayTotal
                d -= 1
            
            if total == s:
                res = mid
                h = mid - 1 # mid was valid, let's try for smaller
            else:
                l = mid + 1 

        return res