class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == '+':
                a, b = stack.pop(), stack.pop()
                c = a + b
                stack.append(c)
            elif n == '-':
                a, b = stack.pop(), stack.pop()
                c = b-a
                stack.append(c)
            elif n == '*':
                a, b = stack.pop(), stack.pop()
                c = a*b
                stack.append(c)
            elif n == '/':
                a, b = stack.pop(), stack.pop()
                c = int(float(b)/float(a))
                stack.append(c)
            else:
                stack.append(int(n))


        return stack[-1]