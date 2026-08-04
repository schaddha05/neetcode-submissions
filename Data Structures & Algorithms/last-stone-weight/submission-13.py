class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [] 

        for stone in stones:
            heapq.heappush(heap, -stone)


        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if y > x:
                heapq.heappush(heap, -(y-x))
        
        return 0 if not heap else -heap[0]
            