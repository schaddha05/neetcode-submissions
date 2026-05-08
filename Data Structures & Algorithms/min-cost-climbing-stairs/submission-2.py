class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def recursive(i, cache):
            if i == len(cost):
                return 0
            if i > len(cost):
                return float('inf')
            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(recursive(i+1, cache),recursive(i+2, cache))
            return cache[i] 
            
        return min(recursive(0, {}), recursive(1, {})) 