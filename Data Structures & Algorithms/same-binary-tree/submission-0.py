# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p and q is None:
            return False
        elif p is None and q:
            return False
        elif p.val != q.val:
            return False
        else:
            l = self.isSameTree(p.left, q.left)
            r = self.isSameTree(p.right, q.right)
            if not l or not r:
                return False
            return True

        