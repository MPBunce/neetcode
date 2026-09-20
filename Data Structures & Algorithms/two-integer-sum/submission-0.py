class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        finder = defaultdict(int)
        for i in range( len(nums) ):
            complement = target - nums[i]
            if complement in finder:
                return [ finder[complement], i ]
            else:
                finder[ nums[i] ] = i

        return False