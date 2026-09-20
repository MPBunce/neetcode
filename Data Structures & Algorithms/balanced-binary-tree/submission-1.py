# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def dfs(root):
            if root is None:
                return 0
            l = dfs(root.left) +1
            r = dfs(root.right) +1
            diff = abs(l-r)
            print(diff)
            if diff > 1 and res[0] == True:
                res[0] = False
            return max(l,r)
        dfs(root)
        return res[0]
        
