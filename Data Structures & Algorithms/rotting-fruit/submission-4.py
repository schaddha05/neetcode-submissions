from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        n = len(grid)
        m = len(grid[0])
        q = deque()
        fresh = 0 
        def addFruit(r, c):
            nonlocal fresh
            if r not in range(n) or c not in range(m) or (r,c) in visited or grid[r][c] == 0:
                return 
            fresh -= 1
            q.append([r,c])
            visited.add((r,c))


        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0 
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                addFruit(r, c + 1)
                addFruit(r, c - 1)
                addFruit(r + 1, c)
                addFruit(r - 1, c)
            time += 1
        
        return time if fresh == 0 else -1
