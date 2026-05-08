class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if stack:
                    if self.isMatch(stack[-1], c):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0 


    def isMatch(self, c1, c2):
        if c1 == '(' and c2 == ')':
            return True
        elif c1 == '[' and c2 == ']':
            return True 
        elif c1 == '{' and c2 == '}':
            return True
        else:
            return False
