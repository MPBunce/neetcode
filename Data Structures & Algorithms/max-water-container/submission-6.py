class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1
        print(l, r)
        while l < r:
            area_check = min(heights[l], heights[r]) * (r - l)
            width_check = r - l
            min_height_check = min(heights[l], heights[r])
            res = max(area_check, res)


            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1


        return res