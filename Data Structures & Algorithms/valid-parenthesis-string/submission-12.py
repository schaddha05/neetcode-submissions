class Solution:
    def checkValidString(self, s: str) -> bool:
        
        def dfs(i, open, cache):
            if open < 0:
                return False 
            
            if i == len(s):
                return open == 0 
            
            if (i, open) in cache:
                return cache[(i, open)]

            if s[i] == '(':
                cache[(i, open)] = dfs(i+1, open + 1, cache)
            elif s[i] == ')':
                cache[(i, open)] = dfs(i+1, open - 1, cache)
            else:
                cache[(i, open)] = (dfs(i+1, open + 1, cache) or 
                        dfs(i+1, open - 1, cache) or 
                        dfs(i+1, open, cache)) 

            return cache[(i, open)]
        return dfs(0, 0, {})

            
