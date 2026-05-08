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
        
        curr = slow.next 
        prev = slow.next = None 
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt 

        l1 = head 
        l2 = prev 

        while l1 and l2:
            nxt = l1.next 
            l1.next = l2 
            l1 = nxt 
            nxt2 = l2.next 
            l2.next = l1 
            l2 = nxt2 
            


