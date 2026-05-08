from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set() 

        def bfs(r,c):
            q = deque() 
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft() 
                directions = [[-1,0],[1,0],[0,-1],[0,1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < len(grid) and r > -1 and c <len(grid[0]) and c > -1 and (r,c) not in visited and grid[r][c] == '1':
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # so when we find the start of an island, visit all other adjacent 
                # ones that form that island and mark them as visited
                if (r,c) not in visited and grid[r][c] == '1':
                    bfs(r,c) 
                    res += 1
        return res