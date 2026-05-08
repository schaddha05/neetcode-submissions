class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        n = len(heights)
        m = len(heights[0])

        def dfs(r,c, prevHeight, visit):
            if r not in range(n) or c not in range(m) or (r,c) in visit or heights[r][c] < prevHeight:
                return 
            
            visit.add((r,c))
            dfs(r, c+1, heights[r][c], visit)
            dfs(r, c-1, heights[r][c], visit)
            dfs(r+1, c, heights[r][c], visit)
            dfs(r-1, c, heights[r][c], visit)

        for c in range(len(heights[0])):
            dfs(0, c, heights[0][c], pacific)
            dfs(len(heights)-1, c, heights[len(heights)-1][c], atlantic)
        
        for r in range(len(heights)):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, len(heights[0])-1, heights[r][len(heights[0])-1], atlantic)

        return list(pacific & atlantic)


