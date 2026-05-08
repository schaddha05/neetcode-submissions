class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        
        def backtracking(closedP, openP,path):
            if closedP == openP == n:
                results.append(path)
                return 
            
            if openP < n:
                backtracking(closedP,openP+1, path+'(')
            
            if closedP < openP:
                backtracking(closedP +1, openP, path + ')')
        
        backtracking(0,0, '')
        return results


