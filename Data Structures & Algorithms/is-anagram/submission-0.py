class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = defaultdict(int) 

        for i in range( len(s) ):
            m[ s[i] ] += 1
            m[ t[i] ] -= 1
        
        res = [n for n in m.values() if n > 0]
        print(res)

        return len(res) == 0
        