class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = defaultdict(int)

        for i in range( len(nums) ):
            if nums[i] in m.keys():
                return [ m[nums[i]], i ]
            else: 
                m[ target - nums[i]] = i
            #print(m)
        return []