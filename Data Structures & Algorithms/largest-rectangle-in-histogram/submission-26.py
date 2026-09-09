class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftBound = [-1 for _ in range(len(heights))]
        rightBound = [len(heights) for _ in range(len(heights))]

        stack = [] # will contain indices not the heights
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]: 
                stack.pop() 
            
            if stack:
                leftBound[i] = stack[-1]
            
            stack.append(i)
        
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() 
            
            if stack:
                rightBound[i] = stack[-1] 
            
            stack.append(i)
        
       
        res = -float('inf')
        for i in range(len(heights)):
            area = heights[i] * ((rightBound[i] - 1) - (leftBound[i] + 1) + 1)
            res = max(res, area)
        
        return res




