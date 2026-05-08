class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        n = len(grid)
        m = len(grid[0])
        def addRoom(r,c):
            if r not in range(n) or c not in range(m) or (r,c) in visited or grid[r][c] == -1:
                return 
            
            visited.add((r,c))
            q.append([r,c])
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        dist = 0 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist 

                addRoom(r, c + 1)
                addRoom(r, c - 1)
                addRoom(r + 1, c)
                addRoom(r - 1, c)
            dist += 1
        
