class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) -3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min (cost[0], cost[1])

        '''
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
        '''
