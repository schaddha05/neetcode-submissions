class Solution:
    import heapq
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = [] # [(distance from x, number)]

        for num in arr:
            dist = abs(num -x)
            heapq.heappush(minHeap, (dist, num))
        
        print(minHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return sorted(res)



