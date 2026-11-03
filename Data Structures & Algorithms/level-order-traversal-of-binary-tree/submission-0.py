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
        
        q = deque()

        q.append((0, root))

        res = []

        while q:
            lvl, node = q.popleft()

            if len(res) == lvl:
                res.append([])

            res[lvl].append(node.val)

            if node.left is not None:
                q.append((lvl + 1, node.left))

            if node.right is not None:
                q.append((lvl + 1, node.right))

        return res
