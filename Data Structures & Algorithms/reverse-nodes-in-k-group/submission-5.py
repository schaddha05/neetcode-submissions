# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        current = head

        while True:
            lastNodeFromPrevGroup = prev
            lastNodeFromCurrGroup = current
            runner = current 
            stop = False
            for _ in range(k):
                if not runner:
                    lastNodeFromPrevGroup.next = current
                    stop = True
                    break 
                runner = runner.next
            
            if stop:
                break 
            i = 0
            while current != None and i < k: # reverse group
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt 
                i += 1
            
            # check if this is the first group we reversed
            if lastNodeFromPrevGroup != None:
                lastNodeFromPrevGroup.next = prev 
            else:
                head = prev 
            
            lastNodeFromCurrGroup.next = current
            if not current:
                break 
            
            prev = lastNodeFromCurrGroup
            

        return head
