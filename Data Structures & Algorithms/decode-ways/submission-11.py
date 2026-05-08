class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(i, cache):
            if i == len(s):
                return 1 
            if s[i] == '0':
                return 0 
            if i in cache:
                return cache[i]
            
            ways = 0 
            ways += dfs(i+1, cache) # single digit 

            if i + 1 < len(s) and int(s[i: i+2]) in range(10,27):
                ways += dfs(i+2, cache)
            
            cache[i] = ways
            return cache[i] 
        
        return dfs(0, {})
            