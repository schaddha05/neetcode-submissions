class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1 
        maxWater = 0
        while left < right:
            area = min(heights[left],heights[right]) * (right-left)
            maxWater = max(area, maxWater)
            if heights[left] >= heights[right]:
                right-=1
            else:
                left+=1
        return maxWater