class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/') 
        stack = []
        print(parts)
        for item in parts: 
            if item == '' or item == '.':
                continue 
            
            if stack and item == '..':
                stack.pop()
            elif not stack and item == '..':
                continue 
            else: 
                stack.append(item)
        
       
        res = '/' + '/'.join(stack) 
        print(res)
        return res
