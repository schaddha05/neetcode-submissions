class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] # (index, height) 

        for i in range(len(heights)):
            left = i 
            while stack and stack[-1][1] > heights[i]: # right boundary found
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                left = index # extend left boundary 
            stack.append((left, heights[i]))
        
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        
        return maxArea
