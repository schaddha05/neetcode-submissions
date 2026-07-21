class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = -float('inf')

        leftLargest = [-1 for _ in range(len(heights))]

        stack = [] # top has leftmost boundary index for each bar
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                leftLargest[i] = stack[-1]
            stack.append(i) 
        
        n = len(heights)
        rightLargest = [n for _ in range(n)]
        stack = [] # top has rightmost boundary index for each bar
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                rightLargest[i] = stack[-1]
            stack.append(i)
        
        for i in range(n):
            res = max(res, heights[i] * (rightLargest[i] - 1 -  (leftLargest[i] + 1) + 1))
        
        return res