class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        cars = [[0,0] for i in range(len(position))]

        for i in range(len(position)):
            cars[i][0] = position[i]
            cars[i][1] = speed[i] 
        cars.sort(reverse = True)

        for i in range(len(cars)):
            time = (target - cars[i][0])/cars[i][1]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


