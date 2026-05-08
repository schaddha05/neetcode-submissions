class TimeMap:

    def __init__(self):
        self.map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''

        l = 0 
        r = len(self.map[key]) -1
        res = '' 
        while l<= r:
            mid = (r + l) // 2
            if self.map[key][mid][1] == timestamp: 
                return self.map[key][mid][0]
            elif self.map[key][mid][1] < timestamp:
                res = self.map[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1 

        return res 
