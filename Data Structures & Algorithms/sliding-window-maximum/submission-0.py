class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, len(nums)
        res = []
        while l < r - k+1:
            sliced = nums[l:l+k]
            print(sliced)
            res.append(max(sliced))
            l+=1
        return res