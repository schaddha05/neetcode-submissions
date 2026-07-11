class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        
        leftMost = [-1 for _ in range(len(heights))]
        stack = [] # top of the stack will have left boundary for each rectangle
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack: 
                leftMost[i] = stack[-1]
            stack.append(i)
        
        n = len(heights)
        rightMost = [n for _ in range(len(heights))]
        stack = [] # top contains right boundary for each rectangle
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            maxArea = max(maxArea, heights[i] * (rightMost[i] - 1 - (leftMost[i] + 1) + 1))
        
        return maxArea

    

