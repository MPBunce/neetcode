class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for char in s:
            if char.isalnum():
                arr.append(char.lower())

        j = "".join(arr)

        return j == j[::-1]