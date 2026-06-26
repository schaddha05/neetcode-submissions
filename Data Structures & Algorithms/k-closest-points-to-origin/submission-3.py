import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x1, x2, y1, y2):
            return math.sqrt( ((x1-x2)**2) + (y1-y2)**2 )
        

        distances = [] # [(distance, point)...]

        for point in points:
            d = distance(0, point[0], 0, point[1])
            distances.append([d, point])
        
        pts = []

        distances.sort()
        for i in range(k):
            pts.append(distances[i][1])
        
        return pts
