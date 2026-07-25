# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = -float('inf')

        # reverse second half of linked list
        slow, fast = head, head
        prev_slow = None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        prev_slow.next = None
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        curr1 = head
        curr2 = prev

        while curr1 and curr2:
            maxSum = max(curr1.val + curr2.val, maxSum)
            curr1 = curr1.next
            curr2 = curr2.next 
        
        return maxSum
        
