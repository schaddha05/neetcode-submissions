class Solution:
    def climbStairs(self, n: int) -> int:
        
        def recursive(i, cache):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = recursive(i+1, cache) + recursive(i+2, cache)
            return cache[i]
        
        return recursive(0, {})



