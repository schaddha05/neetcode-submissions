class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity 
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        cur = self.cache[key]

        # delete node
        newCur = Node(cur.key, cur.val)
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        cur.prev = None
        
        # move to tail (most recently used)
        self.tail.prev.next = newCur
        newCur.prev = self.tail.prev
        self.tail.prev = newCur
        newCur.next = self.tail
        self.cache[key] = newCur

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            cur = self.cache[key]
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.prev = None 

        elif len(self.cache) == self.capacity: # at max, remove LRU
            cur = self.head.next
            curKey = cur.key
            self.head.next = cur.next
            cur.next.prev = self.head
            del self.cache[curKey]
        
        # add new node to end (MRU) and cache
        newNode = Node(key, value)
        self.tail.prev.next = newNode
        newNode.prev = self.tail.prev
        self.tail.prev = newNode
        newNode.next = self.tail
        self.cache[key] = newNode
        
