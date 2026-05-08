class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxNums = []

        for i in range(len(nums)-k+1):
            maximum = nums[i]
            for j in range(i+1, i+k):
                maximum = max(maximum, nums[j])
            maxNums.append(maximum)
        return maxNums