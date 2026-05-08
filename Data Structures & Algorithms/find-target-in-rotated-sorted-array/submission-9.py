class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        h = len(nums) - 1 

        while l <= h:
            m = (h + l) // 2 
            if nums[m] == target:
                return m 
            
            # left sorted portion check
            if nums[m] >= nums[l]:
                if target < nums[l]:
                    l = m + 1 
                elif target > nums[m]:
                    l = m + 1 
                else:
                    h = m - 1
            else: # right sorted portion
                if target > nums[h]:
                    h = m - 1
                elif target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1 
        return -1