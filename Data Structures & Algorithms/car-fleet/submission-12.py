class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 
        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs.sort(reverse = True)
        for car in pairs:
            time = (target - car[0])/ car[1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)