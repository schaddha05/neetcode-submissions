class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums) - 1 
        minimum = nums[start]
        while start <= end:
            if nums[start] < nums[end]:
                minimum = min(minimum, nums[start])
            mid = (end + start) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1

          
            
        return minimum 