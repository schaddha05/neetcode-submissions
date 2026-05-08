class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1, skip1 = 0, 0

        for x in nums[1:]:
            new_rob = x + skip1
            new_skip = max(rob1, skip1)
            rob1, skip1, = new_rob, new_skip
        
        rob2, skip2, = 0, 0 
        for x in nums[:-1]:
            new_rob = x + skip2
            new_skip = max(rob2, skip2)
            rob2, skip2, = new_rob, new_skip

        return max(rob1, skip1, rob2, skip2)
