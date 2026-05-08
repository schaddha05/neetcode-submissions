from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for s, d, w in times:
            adj[s].append([d, w])
        
        shortest = {} 
        minHeap = [[0, k]]

        while minHeap:
            d, curr = heapq.heappop(minHeap) 
            if curr in shortest:
                continue
            shortest[curr] = d
            for neighbor, weight in adj[curr]:
                if neighbor not in shortest:
                    heapq.heappush(minHeap, [d + weight, neighbor])

        return max(shortest.values()) if len(shortest) == n else -1


