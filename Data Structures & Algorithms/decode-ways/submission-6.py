class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 0
        curr = 0 
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = dp1 # single digit decode
                if i + 1 < len(s) and int(s[i: i + 2]) in range(10,27): # double digit decoding
                    curr += dp2
            
            dp1, dp2 = curr, dp1

        return dp1 

            
            

            

            

            