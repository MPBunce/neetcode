class Solution:
    def isValid(self, s: str) -> bool:
        m = { ')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in m and stack:
                if stack[-1] == m[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0