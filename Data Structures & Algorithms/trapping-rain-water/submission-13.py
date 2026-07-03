class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0 
        prefix = [0 for _ in range(len(height))]
        suffix = [0 for _ in range(len(height))]

        prevLeft = height[0] 
        prevRight = height[len(height)-1] 
        for i in range(1,len(height)):
            prefix[i] = prevLeft
            if height[i] > prevLeft:
                prevLeft = height[i]
           
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = prevRight
            if height[i] > prevRight:
                prevRight = height[i]
        
        for i in range(len(height)):
            l = i - 1 
            r = i + 1
            maxLeft = prefix[i]
            maxRight = suffix[i]
            curHeight = height[i]
            if min(maxLeft, maxRight) < curHeight:
                continue
            water += min(maxLeft, maxRight) - curHeight

        return water