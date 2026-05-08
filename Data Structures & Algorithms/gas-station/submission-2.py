class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue

            tank = gas[i] - cost[i]
            j = (i + 1) % len(cost)
            while j != i:
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    break
                j = (j + 1) % len(cost)
            
            if j == i:
                return j
            
        return -1