# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None and root is None:
            return True

        if subRoot is None or root is None:
            return False

        return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()

        q.append(root)

        while q:
            node = q.popleft()

            if self.isSameTree(node, subRoot):
                return True

            if node is not None:
                q.append(node.left)
                q.append(node.right)

        return False
                
