class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        notVal = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[notVal] = nums[i]
                notVal += 1
        
        return notVal
