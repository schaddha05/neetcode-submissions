class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[len(s)] = 1 # reached end of string, found a valid way

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue 
            
            dp[i] = dp[i+1] # single digit 
            if i + 1 < len(s) and int(s[i: i +2]) in range(10, 27):
                dp[i] += dp[i+2] # double digit encoding
            
        return dp[0] 
             

            