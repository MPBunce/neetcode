class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed = []
        for c in s:
            if c.isalnum():
                trimmed.append(c.lower())
        a = b = "".join(trimmed)
        print(a)
        return a == b[::-1]