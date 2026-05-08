class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if stack:
                    if c == ']' and stack[-1] == '[':
                        stack.pop()
                    elif c == ')' and stack[-1] == '(':
                        stack.pop()
                    elif c == '}' and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False 
                else:
                    return False
        
        return len(stack) == 0 