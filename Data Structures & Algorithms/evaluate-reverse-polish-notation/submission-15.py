class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = '+-/*'
        for n in tokens:
            if n in operators:
                if n == '+':
                    num = int(s[-2]) + int(s[-1])
                elif n == '-':
                    num = int(s[-2]) - int(s[-1])
                elif n == '*':
                    num = int(s[-2]) * int(s[-1])
                else:
                    num = int(int(s[-2]) / int(s[-1]))
                s.pop()
                s.pop()
                s.append(num)
            else:
                s.append(n)

        return int(s[-1])

