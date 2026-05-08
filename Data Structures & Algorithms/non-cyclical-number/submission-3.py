class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True 
        def sumSquareDigits(num):
            strNum = str(num)
            total = 0
            for number in strNum:
                total += int(number) ** 2
            print(total)
            return total 
        
        seen = set()
        curr = n
        while True:
            curr = sumSquareDigits(curr) 
            if curr in seen and curr != 1:
                return False
            if curr == 1:
                return True

            seen.add(curr)
        


            
