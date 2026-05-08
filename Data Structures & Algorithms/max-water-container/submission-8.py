class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0 
        l = 0 
        r = len(heights) -1 

        while l < r and l < len(heights) and r > -1:
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(area, maxArea)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea