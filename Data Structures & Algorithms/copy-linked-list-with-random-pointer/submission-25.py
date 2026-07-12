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
        table = {None: None} # original node -> copy 

        cur = head
        # initially create copies, assign next and random in second pass
        while cur:
            copy = Node(cur.val)
            table[cur] = copy 
            cur = cur.next
        
        current = head
        while current:
            copy = table[current]
            copy.next = table[current.next]
            copy.random = table[current.random]
            current = current.next
        
        return table[head]
        


