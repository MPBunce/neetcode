class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
        res = [0] * (len(nums) * 2)

        for i in range( len(nums) ):
            print(res)
            res[i] = nums[i]
            res[i + nums[i]] = nums[i]


        return res