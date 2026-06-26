class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket = [0, 0, 0]

        for i in range(len(nums)):
            bucket[nums[i]] += 1
        
        j = 0 # keeps track of index in nums

        for i in range(3):
            for k in range(bucket[i]):
                nums[j] = i
                j += 1
        





        