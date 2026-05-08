class Solution:
    import heapq
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for s, d, price in flights:
            adj[s].append((d, price))
        

        shortest = {} # maps end node to price
        minHeap = [(0, src, 0)] # (price, node, stops)
        best_cost = [float('inf')] * n
        best_stops = [float('inf')] * n
        best_cost[src] = 0
        best_stops[src] = 0 

        while minHeap:
            p, curr, stops = heapq.heappop(minHeap)
            if curr == dst:
                return p 
            if stops > k:
                continue 
            if stops <=k+1:
                shortest[curr] = p
            
            for neighbor, price in adj[curr]:
                new_price = price + p 
                if new_price < best_cost[neighbor] or stops + 1 < best_stops[neighbor]:
                    best_cost[neighbor] = new_price
                    best_stops[neighbor] = stops + 1                
                    heapq.heappush(minHeap, (new_price, neighbor, stops + 1))


        return -1