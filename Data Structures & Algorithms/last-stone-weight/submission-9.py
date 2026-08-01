class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            y = -heapq.heappop(heap) 
            x = -heapq.heappop(heap)
            if y > x:
                heapq.heappush(heap, -(y-x))
            
        return -heap[0] if heap else 0

