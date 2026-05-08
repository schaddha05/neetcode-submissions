class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append([value, timestamp])
        else:
            self.hashmap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap.get(key,[])
        left = 0 
        right = len(values) - 1
        result = ""
        while left<= right:
            mid = (right + left)//2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result
                


        
