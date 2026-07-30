class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        openCount = 0 
        closedCount = 0 

        def dfs(path):
            nonlocal openCount
            nonlocal closedCount 
            if len(path) == 2 * n:
                res.append(''.join(path))
                return 
            
            if closedCount > openCount:
                return # malformed parentheses 
            
            if openCount < n:
                path.append("(")
                openCount += 1
                dfs(path)
                path.pop()
                openCount -= 1
            
            if closedCount < n:
                path.append(")")
                closedCount += 1
                dfs(path)
                path.pop()
                closedCount -= 1

        dfs([])
        return res
