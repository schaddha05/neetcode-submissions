class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        def dfs(i, cache):
            if i == len(s):
                return True 
            if i in cache:
                return cache[i] 

            for j in range(i+1, len(s)+1):
                if s[i: j] in wordDict:
                    if dfs(j, cache):
                        cache[i] = True # the substring starting from index i can be segmented 
                        return cache[i] 
                
            cache[i] = False
            return cache[i] 
        
        return dfs(0, {})