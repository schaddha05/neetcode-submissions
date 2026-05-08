# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next 
        
        remove = length - n
        if remove == 0:
            return head.next

        current = head
        for _ in range(remove-1):
            current = current.next 
        
        current.next = current.next.next 
        return head