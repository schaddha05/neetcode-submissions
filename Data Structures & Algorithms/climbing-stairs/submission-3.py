class Solution:
    def climbStairs(self, n: int) -> int:
        
        def recursive(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            return recursive(i+1) + recursive(i + 2)
        
        return recursive(0)



