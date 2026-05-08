class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for d in digits:
            num += str(d)

        return list(str(int(num) + 1))
