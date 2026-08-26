# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def rec(root: Optional[TreeNode]) -> tuple[int, bool]:
            if root is None:
                return (0, True)

            left, leftValid = rec(root.left)

            if not leftValid:
                # print(f"Left not valid at {root.val}")
                return (-1, False)

            right, rightValid = rec(root.right)

            if not rightValid:
                # print(f"Right not valid at {root.val}")
                return (-1, False)

            if abs(left - right) > 1:
                # print(f"Tree not balanced at {root.val}")
                return (-1, False)

            return (max(left, right) + 1, True)

        _, valid = rec(root)

        return valid
