class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]

        i = 0
        cur = 1 
        while i < len(nums) - 1:
            cur *= nums[i]
            prefix[i + 1] = cur
            i += 1

        print(prefix)
        postfix = [1 for _ in range(len(nums))]

        j = len(nums) - 1
        cur = 1
        while j > 0:
            cur *= nums[j]
            postfix[j-1] = cur
            j -= 1

        res = []

        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res