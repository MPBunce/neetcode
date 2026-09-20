# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])

        while queue:
            temp = queue.copy()
            for i in range(len(temp)):
                queue.popleft()
            test = []
            for n in temp:
                if n:
                    test.append(n.val)
            print(test)
            if test:
                res.append(test)
            for n in temp:
                if n:
                    queue.append(n.left)
                    queue.append(n.right)

        print(res)
        return res