class Solution:
    from collections import deque 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] 

        q = deque() # front of queue will always contain the maximum of current window
        l = 0 
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop() 
            
            # get rid of stale indices
            while q and q[0] < l:
                q.popleft() 
            
            if q and nums[r] > nums[q[0]]: 
                q.appendleft(r) 
            else:
                q.append(r) 
            
            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1
            
        return res
