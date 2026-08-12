class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = -float('inf')
        maxLeft = [-1 for _ in range(len(heights))]

        stack = [] # stores indices
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() 
            
            if stack:
                maxLeft[i] = stack[-1]
            stack.append(i)
        
        stack = []
        maxRight = [len(heights) for _ in range(len(heights))]

        for i in range(len(heights) -1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() 
            
            if stack:
                maxRight[i] = stack[-1]
            stack.append(i)
        
        for i in range(len(heights)):
            length = (maxRight[i] - 1) - (maxLeft[i] + 1) + 1
            area = length * heights[i] 
            res = max(res, area)
        
        return res


            

            

        

