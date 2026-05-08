class Solution:
    import heapq
    from collections import defaultdict
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                adj[tuple(points[i])].append([tuple(points[j]), distance])
                adj[tuple(points[j])].append([tuple(points[i]), distance])
        
        minHeap = []
        for point, distance in adj[tuple(points[0])]:
            heapq.heappush(minHeap, (distance, tuple(points[0]), tuple(point)))
        
        visited = set()
        visited.add(tuple(points[0]))
        total = 0
        while minHeap:
            w1, n1, n2 = heapq.heappop(minHeap) 
            if n2 in visited:
                continue
            total += w1
            visited.add(n2)
            for neighbor, weight in adj[n2]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (weight, n2, neighbor))

        return total



