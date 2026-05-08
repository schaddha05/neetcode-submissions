class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0 
        visited = set()

        def dfs(r, c, curArea):
            nonlocal area
            if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            return 1 + (dfs(r,c+1,curArea + 1) + dfs(r,c-1,curArea + 1) + dfs(r+1,c,curArea + 1) + dfs(r-1,c,curArea + 1))
            
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == 1:
                    area = max(area, dfs(r,c,1))
        return area