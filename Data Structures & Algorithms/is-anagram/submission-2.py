class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = defaultdict(int)
        for i in range( len(s) ):
            m[ s[i]] += 1
            m[ t[i]] -= 1
            
        for n in m:
            if m[n] != 0:
                return False
        return True