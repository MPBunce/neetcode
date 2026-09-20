class Solution:
    def sortArray(self, nums2: List[int]) -> List[int]:
        nums = nums2
        for i in range( len(nums) ):
            for j in range(1+i, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp

        return nums