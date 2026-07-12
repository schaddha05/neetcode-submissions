# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        
        previous = None
        current = head
        for i in range(length - n):
            previous = current
            current = current.next 
        
        if not previous: # trying to remove head    
            return head.next
        else:
            previous.next = current.next
            return head
