class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s2)
        window = len(s1)
        while l <= r - window:
            sl = s2[l:l+window:1]
            if sorted(sl) == sorted(s1):
                return True
            l+=1

        return False