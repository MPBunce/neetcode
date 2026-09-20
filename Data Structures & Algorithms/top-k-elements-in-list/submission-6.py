class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)
        #print(counter)
        for i in range(k):
            k_copy = 0
            m = 0
            for k, v in counter.items():
                #print(k, v)
                if v > m:
                    k_copy = k
                    m = v
            res.append(k_copy)
            del counter[k_copy]
        return res