class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split('/')
        stack = []
        for item in items:
            if item == '' or item == '.':
                continue 
            
            if stack and item == '..':
                stack.pop()
                stack.pop()
            elif len(stack) == 0 and item == '..':
                continue
            else:
                stack.append(item)
                stack.append('/')
        
        if stack:
            stack.pop() 
        
        return '/' + ''.join(stack)