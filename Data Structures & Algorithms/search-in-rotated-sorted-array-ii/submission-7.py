class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0 
        h = len(nums) - 1 

        while l <= h:
            mid = (h+l) // 2
            if nums[mid] == target:
                return True 
            
            if nums[mid] == nums[l] == nums[h]:
                l += 1
                h -= 1
                continue 

            if nums[mid] >= nums[l]: # in left sorted portion
                if target < nums[l]:
                    l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1 
                else:
                    h = mid - 1
            else:
                if target > nums[h]:
                    h = mid - 1
                elif target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1 
        
        return False