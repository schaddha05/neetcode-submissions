class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []

        for i, temp in enumerate(temperatures):
            while s and temp > temperatures[s[-1]]:
                res[s[-1]] = i - s[-1]
                s.pop() 

            s.append(i)  

        return res    
