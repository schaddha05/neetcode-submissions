class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        prevRow = [0] * (len(text2) + 1) 
        for i in range(1, len(text1) + 1):
            curRow = [0] * (len(text2) + 1)
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    curRow[j] = 1 + prevRow[j-1]
                else:
                    curRow[j] = max(prevRow[j], curRow[j-1])
            prevRow = curRow
        
        return prevRow[-1]

        '''
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)][len(text2)]
        '''