class ListNode:
    def __init__(self, val):
        self.val = val
        self.nxt = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1 
        
        cur = self.head
        for i in range(index + 1):
            cur = cur.nxt

        return cur.val
           
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        prevFirst = self.head.nxt 
        self.head.nxt = node
        node.nxt = prevFirst
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        cur = self.head.nxt 
        while cur.nxt != None:
            cur = cur.nxt
        
        cur.nxt = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            prev = self.head
            for i in range(index):
                prev = prev.nxt

            node = ListNode(val)
            node.nxt = prev.nxt
            prev.nxt = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= 0 and index < self.size:
            cur = self.head
            for i in range(index):
                cur = cur.nxt
            cur.nxt = cur.nxt.nxt
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)