class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def sign(x):
            if x < 0:
                return -1 
            elif x > 0:
                return 1
           
        # collision only happens when a right moving asteroid comes before a left moving asteroid, so top of stack is right moving, and incoming asteroid is left moving 
        for i in range(len(asteroids)):
            noAppend = False
            while stack and sign(stack[-1]) == 1 and sign(asteroids[i]) == -1: # they will collide
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    noAppend = True 
                    break 
                elif abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                else:
                    noAppend = True
                    break
                
            if not noAppend:
                stack.append(asteroids[i])
        
        return stack