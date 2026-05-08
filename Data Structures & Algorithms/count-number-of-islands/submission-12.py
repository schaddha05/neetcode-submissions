class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0 
        def dfs(r,c):
            if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in visited or grid[r][c] == '0':
                return 
            
            visited.add((r,c))

            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == '1':
                    islands += 1 
                    dfs(r,c) 
        
        return islands 