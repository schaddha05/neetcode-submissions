# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head 
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        current = slow.next 
        prev = slow.next = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        l2 = prev

        while l1 and l2:
            nxt = l1.next
            l1.next = l2
            l1 = nxt
            nxt2 = l2.next
            l2.next = l1
            l2 = nxt2

     
       

        


