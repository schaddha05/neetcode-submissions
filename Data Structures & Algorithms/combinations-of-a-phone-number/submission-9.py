class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        hmap = {2: "abc",
                3: "def",
                4: "ghi",
                5: "jkl",
                6: "mno",
                7: "pqrs",
                8: "tuv",
                9: "wxyz"}
        
        def dfs(i, curStr):
            if i == len(digits):
                res.append(curStr)
                return 
            
            for c in hmap[int(digits[i])]: 
                dfs(i+1, curStr + c) 
              
        dfs(0, '') 

        return res




