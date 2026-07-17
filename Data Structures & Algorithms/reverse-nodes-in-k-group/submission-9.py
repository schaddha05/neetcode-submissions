# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        groupPrev = dummy 

        while True:
            # 1. get kth node if it exists
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next

            # 2. reverse current group of k nodes
            prev = kth.next
            curr = groupPrev.next 
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt 
            
            tmp = groupPrev.next
            groupPrev.next = kth # the tail after reversal of previous group must point to head of current group
            groupPrev = tmp

        return dummy.next



    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr