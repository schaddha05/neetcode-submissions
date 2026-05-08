class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for s,d,w in edges:
            adj[s].append((d,w))

        shortest_paths = {i: float('inf') for i in range(n)}
        shortest_paths[src] = 0

        min_heap = [(0,src)]
        
        while min_heap: 
            w1, n1 = heapq.heappop(min_heap)

            if w1 > shortest_paths[n1]:
                continue 
            
            for n2, w2 in adj[n1]:
                new_dist = w2+ w1
                if new_dist < shortest_paths[n2]:
                    shortest_paths[n2] = new_dist
                    heapq.heappush(min_heap, (new_dist, n2))
        for i in range(n):
            if shortest_paths[i] == float('inf'):
                shortest_paths[i] = -1
        return shortest_paths

