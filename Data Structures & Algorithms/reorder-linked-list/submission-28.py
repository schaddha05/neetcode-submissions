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
        previous = slow.next = None 

        while cur:
            nxt = cur.next
            cur.next = previous
            previous = cur
            cur = nxt
        
        cur1 = head 
        cur2 = previous
        while cur1 and cur2:
            nxt1 = cur1.next 
            cur1.next = cur2
            cur1 = nxt1
            nxt2 = cur2.next
            cur2.next = cur1
            cur2 = nxt2
        
        
        
