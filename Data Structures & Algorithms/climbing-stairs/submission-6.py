class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n 
        
        a = 1 # 0 steps
        b = 1 # 1 step 

        for i in range(2, n+1):
            tmp = b 
            b = a + b
            a = tmp
        
        return b



