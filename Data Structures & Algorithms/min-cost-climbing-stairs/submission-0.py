class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def recursive(i):
            if i == len(cost):
                return 0
            if i > len(cost):
                return float('inf')
            
            return cost[i] + min(recursive(i+1),recursive(i+2))
            
        return min(recursive(0), recursive(1)) 