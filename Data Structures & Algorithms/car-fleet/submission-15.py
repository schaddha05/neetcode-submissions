class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))

        cars.sort()
        stack = []
        for i in range(len(cars) - 1, -1, -1):
            if not stack or cars[i][1] > stack[-1]:   
                stack.append(cars[i][1])

        return len(stack)