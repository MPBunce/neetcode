class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # res[i] = product of all elements before i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # multiply res[i] by product of all elements after i
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res