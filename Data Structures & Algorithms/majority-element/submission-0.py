class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        val = 0
        key = 0
        for k, v in c.items():
            if v > val:
                val = v
                key = k

        return key