class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() 
        res = 0 

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < end:
                res += 1
                end = min(end, interval[1])
            else:
                start = interval[0]
                end = interval[1]
        
        return res