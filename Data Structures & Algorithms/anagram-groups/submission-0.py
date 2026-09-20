class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for n in strs:
            temp = sorted(list(n))
            joined = "".join(temp)
            print(joined, n)
            if joined in res:
                res[joined].append(n)
            else:
                res[joined] = [n]


        return res.values()