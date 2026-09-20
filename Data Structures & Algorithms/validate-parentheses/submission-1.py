class Solution:
    def isValid(self, s: str) -> bool:
        m = { ')':'(', ']':'[', '}':'{'}
        stack = []

        for character in s:
            if character in m: 
                if not stack or stack[-1] != m[character]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(character)
            print(stack)

        if not stack:
            return True

        return False