class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for char in s:
            if char.isalnum():
                arr.append( char.lower() )
        s = "".join(arr)
        return s == s[::-1]