# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    import heapq   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        minHeap = []

        # add all nodes to minHeap
        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                heapq.heappush(minHeap, cur.val)
                cur = cur.next 

        dummy = ListNode()
        cur = ListNode(heapq.heappop(minHeap))
        dummy.next = cur
        while minHeap:
            cur.next = ListNode(heapq.heappop(minHeap))
            cur = cur.next
        
        return dummy.next