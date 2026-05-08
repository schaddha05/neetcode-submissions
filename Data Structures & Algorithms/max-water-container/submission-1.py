class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        maxArea = 0
        while left < right:
            curArea = min(heights[left],heights[right]) * (right-left)
            maxArea = max(curArea, maxArea)
            if heights[right] >= heights[left]:
                left+=1
            else:
                right-=1 
        return maxArea
