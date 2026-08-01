# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def mergeTwoLists(head1, head2):
            dummy = ListNode()
            cur = dummy 
            while head1 and head2:
                if head1.val <= head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next 
            if head1:
                cur.next = head1
            if head2:
                cur.next = head2

            return dummy.next # return head of merged list

        while len(lists) > 1: 
            mergedLists = []
            for i in range(1, len(lists), 2):
                mergedLists.append(mergeTwoLists(lists[i-1], lists[i]))

            if len(lists) % 2 != 0:
                mergedLists.append(lists[-1])
            lists = mergedLists
            print(lists)
        
        return lists[0]
                






            