class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i # delete charcters 
            if i == len(word1):
                return len(word2) - j # insert characters
            
            res = 0 
            if word1[i] == word2[j]:
                res += dfs(i+1, j+1)
            else:
                res += 1 + min(dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1))

            return res 
        
        return dfs(0,0)