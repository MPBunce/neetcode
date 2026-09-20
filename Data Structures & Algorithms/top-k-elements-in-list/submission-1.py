class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = defaultdict(int)
        for n in nums:
            mapp[n] += 1
        res = []
        for i in range( k ):
            m = 0
            temp = 0
            for k, v in mapp.items():
                if v > m:
                    temp = k
                    m = v
            res.append(temp)
            del mapp[temp]
        return res
