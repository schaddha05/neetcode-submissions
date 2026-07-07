class Solution:
    import math
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                o = tokens[i]
                x = stack[-2]
                y = stack[-1]
                stack.pop()
                stack.pop()
                if o == '+':
                    stack.append(x+y) 
                elif o == '-':
                    stack.append(x-y)
                elif o == '*':
                    stack.append(x*y)
                else:
                    stack.append(int(x/y))
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]