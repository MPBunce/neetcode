class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            #print(s, n)
            if n in s:
                return n
            s.add(n)

        return -1