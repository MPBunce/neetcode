class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            left_val = nums[l]
            print(l, left_val)
            right_val = nums[r]
            print(r, right_val)
            mid_point = (l+r)//2
            print(mid_point, nums[mid_point])
            print("\n===========\n")

            if nums[mid_point] > nums[r]:
                l = mid_point+1
            else:
                r=mid_point

        return nums[l]