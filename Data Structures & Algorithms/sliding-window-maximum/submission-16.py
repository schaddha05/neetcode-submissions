class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = collections.deque()

        l = 0 
        for r in range(len(nums)):
            # remove elements that are smaller than current since they can't 
            # possibly be max of current window
            while window and nums[r] > nums[window[-1]]:
                window.pop()
            
            # sliding the window by removing stale indices less than left bound
            while window and window[0] < l:
                window.popleft()
            
            if window and nums[r] > nums[window[0]]:
                window.appendleft(r)
            else:
                window.append(r)
            
            if r - l + 1 == k:
                res.append(nums[window[0]])
                l += 1
        
        return res