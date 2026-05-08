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
            length+=1
        
        removeIndex = length - n

        if removeIndex == 0:
            return head.next
            
        current = head
        for i in range(length-1):
            if i+1 == removeIndex:
                current.next = current.next.next
                break 
            current = current.next
        return head
