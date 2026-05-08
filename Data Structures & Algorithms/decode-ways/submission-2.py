class Solution:
    def numDecodings(self, s: str) -> int:
        

        def dfs(i):
            if i == len(s):
                return 1 
            if s[i] == '0':
                return 0 
            
            ways = 0 
            # single digit 
            ways += dfs(i+1)
            
            ways += dfs(i+2) if i + 1 < len(s) and int(s[i: i + 2]) in range(10, 27) else 0

            return ways

        return dfs(0) 
            
            

            

            

            