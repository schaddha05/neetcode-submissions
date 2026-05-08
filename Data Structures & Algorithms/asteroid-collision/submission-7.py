class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            aDestroyed = False
            while stack and a < 0 and stack[-1] > 0: # opposite signs -> collision
                if abs(a) == abs(stack[-1]):
                    stack.pop()
                    aDestroyed = True
                    break 
                elif abs(a) < abs(stack[-1]):
                    aDestroyed = True
                    break
                else:
                    stack.pop()
            
            if not aDestroyed:
                stack.append(a)


        return stack