# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = [0]
        def dfs(node):
            if node is None:
                return 0
            else:
                a = dfs(node.left) + 1
                b = dfs(node.right) + 1
                count[0] = max(a,b)
                return max(a,b)
        dfs(root)
        return count[0]