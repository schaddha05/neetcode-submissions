import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x1, x2, y1, y2):
            return math.sqrt( ((x1-x2)**2) + (y1-y2)**2 )
        

        heap = [] # [(distance, point)...]

        for point in points:
            d = distance(0, point[0], 0, point[1])
            heapq.heappush(heap, [-d, point])
            if len(heap) > k:
                heapq.heappop(heap)
        
        pts = []

        for i in range(k):
            pts.append(heapq.heappop(heap)[1])
        
        return pts
