# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDiameter = 0
        
        def rec(root: Optional[TreeNode]) -> int:
            nonlocal maxDiameter
            if root is None:
                return 0
            
            leftLen = rec(root.left)
            rightLen = rec(root.right)

            depth = max(leftLen, rightLen)
            diameter = leftLen + rightLen

            maxDiameter = max(maxDiameter, diameter)

            return depth + 1

        rec(root)

        return maxDiameter