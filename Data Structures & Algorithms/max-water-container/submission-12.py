class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0 
        r = len(heights) -1 

        while l < r:
            curArea = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, curArea)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return maxArea