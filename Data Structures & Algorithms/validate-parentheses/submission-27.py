class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if len(stack) > 0:
                    if stack[-1] == '(' and c == ')' or stack[-1] == '{' and c == '}' or stack[-1] == '[' and c == ']':
                        stack.pop()
                    else:
                        return False
                else:
                    return False 
        
        return len(stack) == 0