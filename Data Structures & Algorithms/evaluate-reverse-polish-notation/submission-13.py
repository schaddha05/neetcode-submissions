class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = '+-*/'
        stack = []
        for t in tokens:
            if t in operators:
                val1 = stack.pop()
                val2 = stack.pop()
                if t == '+':
                    stack.append(val1 + val2)
                elif t == '-':
                    stack.append(val2 - val1)
                elif t == '*':
                    stack.append(val1 * val2)
                else:
                    stack.append(int(float(val2)/val1))
            else:
                stack.append(int(t))
        return stack[-1]