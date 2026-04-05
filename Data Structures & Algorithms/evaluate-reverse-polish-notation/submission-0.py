class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {'+', '-', '*', '/'}


        for n in tokens:
            if n in operations:
                b = stack.pop()
                a = stack.pop()

                if n == '+':
                    stack.append(a + b)
                elif n == '-':
                    stack.append(a - b)
                elif n == '*':
                    stack.append(a*b)
                elif n == '/':
                    stack.append(int(a/b))

            else:
                stack.append(int(n))

        return stack[0]