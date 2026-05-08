class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumArea = 0
        left = 0 
        right = len(heights) -1 

        while left < right:
            currArea = (right - left) * min(heights[left], heights[right])
            maximumArea = max(maximumArea, currArea)
            if heights[right] >= heights[left]:
                left+=1
            else:
                right-=1
        return maximumArea