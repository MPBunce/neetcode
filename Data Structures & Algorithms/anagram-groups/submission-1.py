class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for n in strs:
            temp = tuple( sorted(n) )
            print(temp)
            m[ temp ].append(n)
        return  [n for n in m.values()]