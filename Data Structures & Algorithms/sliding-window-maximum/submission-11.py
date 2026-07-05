class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()

        l = 0 
        for r in range(len(nums)):
            while window and nums[window[-1]] < nums[r]:
                window.pop()
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



