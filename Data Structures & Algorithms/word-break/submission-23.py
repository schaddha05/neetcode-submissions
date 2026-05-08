class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        def dfs(i, cache):
            if i == len(s):
                return True 
            if i in cache:
                return cache[i]

            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] in wordDict:
                    if dfs(i + len(w), cache):
                        cache[i] = True
                        return True 
            
            cache[i] = False
            return cache[i]  
        
        return dfs(0, {})