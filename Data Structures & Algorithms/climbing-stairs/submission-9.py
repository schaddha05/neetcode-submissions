class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(n, cache):
            if n < 0:
                return 0 # overshot it
            
            if n == 0:
                return 1 # valid way to reach top

            if n in cache:
                return cache[n]

            cache[n] = dfs(n-2, cache) + dfs(n-1, cache) 
            return cache[n]

        return dfs(n, {})