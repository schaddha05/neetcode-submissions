class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0 
        prefix = [0 for _ in range(len(height))]
        suffix = [0 for _ in range(len(height))]

        for i in range(1,len(height)):
            prefix[i] = max(height[:i])

        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(height[i+1:])
        
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