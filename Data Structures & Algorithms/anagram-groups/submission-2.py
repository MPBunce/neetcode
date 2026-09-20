class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        res = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            m[sorted_s].append(s)
        for n in m.values():
            res.append(n)
        return res