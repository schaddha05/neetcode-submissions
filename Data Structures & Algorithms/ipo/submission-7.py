class Solution:
    import heapq
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = [] # of the affordable projects, select one with highest profit
        minHeap = [] # choose projects with capital <= current capital 

        for i in range(len(capital)):
            minHeap.append([capital[i], profits[i]])
        
        heapq.heapify(minHeap)

        for i in range(k):
            while minHeap and minHeap[0][0] <= w:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap)[1])
            
            if maxHeap:
                w += -heapq.heappop(maxHeap)

        return w




        
