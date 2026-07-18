class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        maxLeft = [0 for _ in range(len(height))]
        maxRight = [0 for _ in range(len(height))]

        maxLeft[0] = height[0]
        maxRight[len(height)-1] = height[-1]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i])

        print(maxLeft)  
        for i in range(len(height)-2, -1, -1):
            maxRight[i] = max(maxRight[i + 1],height[i])
        
        print(maxRight)
        for i in range(len(height)):
            trapped = min(maxLeft[i], maxRight[i]) - height[i]
            if trapped > 0:
                res += trapped
        
        return res