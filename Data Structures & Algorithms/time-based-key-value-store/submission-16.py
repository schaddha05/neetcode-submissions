class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l = 0
        r = len(self.timeMap[key]) - 1
        while l <= r:
            mid = (r + l) // 2
            if self.timeMap[key][mid][0] <= timestamp:
                res = self.timeMap[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1

        
        return res

