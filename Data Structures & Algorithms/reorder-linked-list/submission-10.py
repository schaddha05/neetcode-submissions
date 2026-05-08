# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        cur = slow.next 
        prev = slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt 
        
        l2 = prev
        l1 = head
        while l1 and l2:
            nxt = l1.next
            l1.next = l2
            l1 = nxt
            nxt2 = l2.next
            l2.next = l1
            l2 = nxt2
        
