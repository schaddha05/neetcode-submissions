class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed)) 
        pairs.sort(reverse = True)
        times = []

        for p,s in pairs:
            time = (target-p)/s
            if times and time <= times[-1]:
                continue
            times.append(time)
        
        return len(times)

