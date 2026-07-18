class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [] 

        for i in range(len(position)):
            cars.append((position[i], speed[i])) 
        
        cars.sort() # sort by position 
        stack = []
        for i in range(len(cars) -1, -1, -1):
            time = (target - cars[i][0]) / cars[i][1]
            if not stack or time > stack[-1]:
                stack.append(time)
            
        
        
        return len(stack)

