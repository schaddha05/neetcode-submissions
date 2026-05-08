class Solution:
    from collections import deque 
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]
        inDegree = [0] * (len(edges) + 1)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            inDegree[a] += 1
            inDegree[b] += 1
        
        q = deque()
        for i in range(1, len(edges) + 1):
            if inDegree[i] == 1:
                q.append(i) 

        i = 0     
        while q:
            curr = q.popleft()
            inDegree[curr] -= 1
            for n in adj[curr]:
                inDegree[n] -= 1
                if inDegree[n] == 1:
                    q.append(n) 

        for a,b in reversed(edges):
            if inDegree[b] == 2 and inDegree[a]:
                return [a,b]

