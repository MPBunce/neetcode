class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = []
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for n in range(k):
            c_max = 0
            c_key = 0
            for key in counter:
                if counter[key] > c_max:
                    c_max = counter[key]
                    c_key = key
            res.append(c_key)
            counter.pop(c_key)
            
        return res