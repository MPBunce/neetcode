class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == '+':
                a,b = stack.pop(), stack.pop()
                temp = b + a
                stack.append(temp)
            elif n == '-':
                a,b = stack.pop(), stack.pop()
                temp = b-a
                stack.append(temp)
            elif n == '*':
                a,b = stack.pop(), stack.pop()
                temp = a * b
                stack.append(temp)
            elif n == '/':
                a,b = stack.pop(), stack.pop()
                temp = int( float(b) / float(a) )
                stack.append(temp) 
            else:
                stack.append( int(n) )

        return stack[-1]