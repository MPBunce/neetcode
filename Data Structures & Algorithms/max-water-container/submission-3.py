class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        res = 0
        while l < r:
            h = min(heights[r], heights[l])
            w = r - l
            res = max(res, w*h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res