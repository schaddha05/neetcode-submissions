class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                left.append(i)
            if ch == '*':
                star.append(i) 
            
            if ch == ')':
                if left:
                    left.pop() 
                elif star:
                    star.pop()
                else:
                    return False
        
        while left and star:
            if left[-1] > star[-1]:
                return False 
            left.pop()
            star.pop()
          
        
        return len(left) == 0  


            
