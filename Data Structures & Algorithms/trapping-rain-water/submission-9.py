class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0 

        for i in range(len(height)):
            l = i - 1 
            r = i + 1
            curHeight = height[i]
            maxLeft = 0 
            maxRight = 0
            while l > -1 or r < len(height): 
                if l > -1 and height[l] > curHeight:
                    maxLeft = max(maxLeft, height[l])
                
                if r < len(height) and height[r] > curHeight:
                    maxRight = max(maxRight, height[r])
                l -= 1
                r += 1

            if min(maxLeft, maxRight) < curHeight:
                continue
            water += min(maxLeft, maxRight) - curHeight

        return water