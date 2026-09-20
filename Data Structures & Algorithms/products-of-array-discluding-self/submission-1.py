class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        pre, post = 1,1
        res = []

        for i in range( len(nums) ):
            pre = nums[i] * pre
            prefix.append(pre)
        for i in range( len(nums)-1, -1, -1):
            post = nums[i] * post
            postfix.append(post)
        postfix = postfix[::-1]            

        for i in range( len(prefix)):
            if i == 0:
                res.append(1 * postfix[i+1])
            elif i == len(prefix)-1:
                res.append(prefix[i-1] * 1)
            else:
                res.append(prefix[i-1] * postfix[i+1])
        return res