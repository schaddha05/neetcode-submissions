class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
       
        # guranteed to return because we don't need to update any more digits 
        if digits[i] != 9:
            digits[i] = digits[i] + 1
            return digits 
        
        while digits[i] == 9 and i >= 0:
            digits[i] = 0
            i -= 1
        if i < 0:
            digits.insert(0, 1)
        else:
            digits[i] += 1 
        
        return digits

                