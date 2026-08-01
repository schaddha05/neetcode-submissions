class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # heap to keep track of top k largest numbers, where kth largest at root 
        self.heap = nums 
        heapq.heapify(self.heap) 

        print(self.heap)
        # heap should contain top k numbers, not everything in nums
        while len(self.heap) > k:
            heapq.heappop(self.heap)

        print(self.heap)


       

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
        
        return self.heap[0]

        
