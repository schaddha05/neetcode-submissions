class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [] 

        def backtrack(openP, closeP, path):
            if openP == closeP == n:
                result.append(path)
                return 
            
            if openP < n:
                backtrack(openP+1, closeP, path + '(')
            
            if closeP < openP:
                backtrack(openP, closeP+1, path + ')')
        
        backtrack(0,0, '')

        return result