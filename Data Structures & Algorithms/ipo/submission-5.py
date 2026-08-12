class Solution:
    import heapq
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = [] # profits of projects we can afford 
        minHeap = [] # root contains project with smallest capital 

        for i in range(len(capital)):
            minHeap.append([capital[i], profits[i]]) 

        heapq.heapify(minHeap)
        res = w 

        for i in range(k):
            while minHeap and minHeap[0][0] <= res:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap)[1])

            if maxHeap:
                res += -heapq.heappop(maxHeap)

        return res
        
            

            





        





