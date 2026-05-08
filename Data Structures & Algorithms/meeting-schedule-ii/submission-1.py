"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        minRooms = 0 
        minHeap = [] 

        for i in range(len(intervals)): 
            while minHeap and intervals[i].start >= minHeap[0]:
                heapq.heappop(minHeap) 

            heapq.heappush(minHeap, intervals[i].end)
            minRooms = max(len(minHeap), minRooms)
        
        return minRooms