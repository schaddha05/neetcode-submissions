"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {} 
        cur = head 
        while cur:
            copies[cur] = Node(cur.val) 
            cur = cur.next 
        copies[None] = None

        curr = head
        while curr: 
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random] 
            curr = curr.next 
        return copies[head]