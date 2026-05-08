class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 
        

        prevRow = [False] * (len(s2)+1) 
        prevRow[0] = True 

        for j in range(1, len(s2) + 1):
            prevRow[j] = prevRow[j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, len(s1)+1):
            curRow = [False] * (len(s2) + 1)
            curRow[0] = prevRow[0] and (s1[i-1] == s3[i-1])
            for j in range(1, len(s2)+1):
                take_from_s1 = prevRow[j] and (s1[i - 1] == s3[i + j - 1])   # up
                take_from_s2 = curRow[j - 1] and (s2[j - 1] == s3[i + j - 1]) # left
                curRow[j] = take_from_s1 or take_from_s2
            prevRow = curRow

        return prevRow[len(s2)]
