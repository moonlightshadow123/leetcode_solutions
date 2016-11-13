import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = set(['+', '-', '*', '/'])
        stack = []
        for token in tokens:
            if token in operators:
                y = stack[-1]
                del stack[-1]
                x = stack[-1]
                del stack[-1]
                stack.append(self.operate(x, y, token))
            else:
                stack.append(int(token))
        return stack[-1]
    def operate(self, x, y, token):
        if token == '+':
            return x + y
        elif token == '-':
            return x - y
        elif token == '*':
            return x * y
        elif token == '/':
            if x*y < 0:
                return int(math.ceil(float(x) / y))
            else:
                return x / y
        
