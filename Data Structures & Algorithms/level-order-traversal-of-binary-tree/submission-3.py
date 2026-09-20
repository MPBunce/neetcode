# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque([root])
        while q:
            qc = q.copy()
            for i in range(len(qc)):
                q.popleft()
            t = []
            for n in qc:
                t.append(n.val)
            res.append(t)
            for n in qc:
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return res