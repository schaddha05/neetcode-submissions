class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()

        for n in nums:
            if n in unique:
                return n
            unique.add(n)
        