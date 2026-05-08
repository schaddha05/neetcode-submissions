class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set() 

        def dfs(r,c):
            nonlocal res
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or (r,c) in visited or grid[r][c] == '0':
                return 
            
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # so when we find the start of an island, visit all other adjacent 
                # ones that form that island and mark them as visited
                if (r,c) not in visited and grid[r][c] == '1':
                    res += 1
                    dfs(r,c) 
        return res