class MedianFinder:
    import heapq 
    def __init__(self):
        self.small = [] # maxHeap for smaller half of numbers
        self.large = [] # minHeap for larger half of numbers 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # move from small to large if num is in wrong heap 
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val) 
        
        # uneven sizes 
        if len(self.small) - len(self.large) > 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        # even length list
        return (-self.small[0] + self.large[0]) / 2
        
        