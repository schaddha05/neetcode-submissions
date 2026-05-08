class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [] 
        
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(end, interval[1]) 
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1] 
        
        res.append([start, end])
        return res