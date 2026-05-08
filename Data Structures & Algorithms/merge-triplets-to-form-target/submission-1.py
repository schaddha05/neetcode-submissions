class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for t in triplets:
            if max(t) > max(target):
                triplets.remove(t) 
        
        for i in range(len(target)):
            n = target[i]
            found = False
            for t in triplets:
                if t[i] == n:
                    found = True
            if not found:
                return False 
        
        return True
