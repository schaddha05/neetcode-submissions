class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prevRow = [0] * (len(word2) + 1)
        
        for j in range(len(word2) + 1):
            prevRow[j] = j # only inserts
        
        for i in range(1, len(word1) + 1):
            curRow = [0] * (len(word2) + 1) 
            curRow[0] = prevRow[0] + 1
            for j in range(1, len(word2) +1):
                if word1[i-1] == word2[j-1]:
                    curRow[j] = prevRow[j-1]
                else:
                    curRow[j] = 1 + min(prevRow[j], curRow[j-1], prevRow[j-1])
            prevRow = curRow

        return prevRow[-1]
        
        '''
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i # only deletes
        
        for j in range(len(word2) + 1):
            dp[0][j] = j # only inserts
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) +1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[len(word1)][len(word2)]
        '''
