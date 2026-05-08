class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.start = Node(0,0) 
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start
        self.capacity = capacity 

    def insert(self, node):
        prev = self.end.prev 
        nxt = self.end 
        node.next = nxt 
        node.prev = prev
        prev.next = node 
        nxt.prev = node

    def remove(self, node):
        prev = node.prev 
        nxt = node.next 
        prev.next = nxt 
        nxt.prev = prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.start.next 
            self.remove(lru) 
            del self.cache[lru.key]