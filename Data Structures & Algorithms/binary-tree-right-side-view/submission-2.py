# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            level = queue.copy()
            print(level)
            if level[-1]:
                res.append( level[-1].val )
            for n in range( len(level) ):
                queue.popleft()
            for node in level:
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            
        return res