class Solution:
    from collections import deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[]  for _ in range(numCourses)]
        inDegree = [0] * numCourses 

        for a, b in prerequisites:
            adj[b].append(a)
            inDegree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i) 
        
        i = 0 
        ordering = [0] * numCourses
        while q:
            curr = q.popleft()
            ordering[i] = curr 
            i += 1
            for neighbor in adj[curr]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)
        
        if i != numCourses:
            return False
        return True 


        
