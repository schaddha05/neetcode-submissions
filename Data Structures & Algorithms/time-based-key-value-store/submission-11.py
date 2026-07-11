class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap or timestamp < self.timeMap[key][0][0]:
            return ""
        
        l = 0 
        r = len(self.timeMap[key]) - 1
        while l <= r:
            mid = (r + l) // 2
            if self.timeMap[key][mid][0] == timestamp:
                return self.timeMap[key][mid][1]
            elif timestamp > self.timeMap[key][mid][0]:
                l = mid + 1
            else:
                r = mid - 1
        
        return self.timeMap[key][r][1]

