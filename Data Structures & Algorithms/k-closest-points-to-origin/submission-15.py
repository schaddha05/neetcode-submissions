class Solution:
    import math
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1, x2, y1, y2):
            return math.sqrt( ((x1-x2)**2) + ((y2-y1)**2) )
        
        res = []
        heap = [] # max heap by distance, each element = (disance, point)
        for point in points: 
            d = distance(0, point[0], 0, point[1]) # distance btwn point and origin

            heapq.heappush(heap, [-d, point])
            if len(heap) > k:
                heapq.heappop(heap) 
        
            
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
