class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 
        
        prevRow = [False] * (len(s2)+1)
        prevRow[0] = True 

        for j in range(1, len(s2) + 1):
            prevRow[j] = prevRow[j-1] and s2[j-1] == s3[j-1] 
        
        for i in range(1, len(s1) + 1):
            curRow = [False] * (len(s2) + 1)
            curRow[0] = prevRow[0] and s1[i-1] == s3[i-1] 
            for j in range(1, len(s2) + 1):
                if (s2[j-1] == s3[i+j-1] and curRow[j-1]) or (s1[i-1] == s3[i+j-1] and prevRow[j]):
                    curRow[j] = True 
            prevRow = curRow

        return prevRow[len(s2)]



        