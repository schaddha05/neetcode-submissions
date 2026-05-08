class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1 # top of staircase
        b = 1 # 1 step away from top

        for i in range(n-1):
            tmp = b 
            b = a + b
            a = tmp
        
        return b



