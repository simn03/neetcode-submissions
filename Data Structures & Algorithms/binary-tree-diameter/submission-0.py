# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def rec(root: Optional[TreeNode]) -> tuple[int, int]:
            if root is None:
                return (0, 0)
            
            leftLen, leftMax = rec(root.left)
            rightLen, rightMax = rec(root.right)

            depth = max(leftLen, rightLen)
            diameter = leftLen + rightLen

            maxDiameter = max(leftMax, rightMax, diameter)

            return (depth + 1, maxDiameter)

        l, d = rec(root)

        return d