class Solution:
    from collections import deque 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque() # front of q will always contain the maximum 
        l = 0 
        for r in range(len(nums)):
            while q and nums[q[-1]] <= nums[r]: # while incoming number bigger than number at end of queue
                q.pop() 
            
            while q and q[0] < l:
                q.popleft()
            
            if q and nums[r] > nums[q[0]]:
                q.appendleft(r) # new maximum found
            else:
                q.append(r)
            
            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1
            
        
        return res