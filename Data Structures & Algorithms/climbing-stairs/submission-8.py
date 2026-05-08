class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(n):
            if n < 0:
                return 0 # overshot it
            
            if n == 0:
                return 1 # valid way to reach top

            return dfs(n-2) + dfs(n-1) 
        
        return dfs(n)