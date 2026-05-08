class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True 
        def sumSquareDigits(num):
            strNum = str(num)
            total = 0
            for number in strNum:
                total += int(number) ** 2
            return total 
        
        slow, fast = n, n 
        while True:
            slow = sumSquareDigits(slow)
            fast = sumSquareDigits(sumSquareDigits(fast))
            if fast == 1:
                return True 

            if slow == fast and fast != 1:
                return False
            
           
        


            
