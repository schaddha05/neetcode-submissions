class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        

        for i in range(len(heights)):
            leftBound = i 

            while leftBound > 0 and heights[leftBound - 1] >= heights[i]:
                leftBound -= 1
            
            rightBound = i
            while rightBound < len(heights) - 1 and heights[rightBound + 1] >= heights[i]:
                rightBound += 1
            
            maxArea = max(maxArea, heights[i] * (rightBound - leftBound + 1))
        
        return maxArea

