# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = [0]
        def find(root, count):
            if root is None:
                return
            else:
                depth[0] = max(depth[0], count)
                find(root.left, count +1)
                find(root.right, count +1)
        find(root, 1)
        return depth[0]
