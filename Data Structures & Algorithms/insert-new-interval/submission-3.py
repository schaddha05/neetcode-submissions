class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # inserted interval
        isInserted = False
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[0] < interval[0]:
                intervals.insert(i, newInterval) 
                isInserted = True 
            
        if not isInserted:
            intervals.append(newInterval)
        
        # merge intervals
        start = intervals[0][0] 
        end = intervals[0][1] 
        res = []
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
            

        