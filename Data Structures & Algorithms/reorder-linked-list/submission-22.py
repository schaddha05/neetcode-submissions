# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        # find middle, which will be at slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
           
        
        # reverse second half of linked lis
        cur = slow.next 
        prev = slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        cur = head 
        while cur and prev: # might change
            nxt1 = cur.next 
            cur.next = prev
            cur = nxt1

            nxt2 = prev.next
            prev.next = cur
            prev = nxt2
        

        


        