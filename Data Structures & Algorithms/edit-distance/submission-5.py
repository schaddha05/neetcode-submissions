class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def dfs(i, j, cache):
            if j == len(word2):
                return len(word1) - i # delete charcters 
            if i == len(word1):
                return len(word2) - j # insert characters
            if (i,j) in cache:
                return cache[(i,j)]
            res = 0 
            if word1[i] == word2[j]:
                res += dfs(i+1, j+1, cache)
            else:
                res += 1 + min(dfs(i, j+1, cache), dfs(i+1, j, cache), dfs(i+1, j+1, cache))

            cache[(i,j)] = res
            return cache[(i,j)]
        
        return dfs(0,0, {})