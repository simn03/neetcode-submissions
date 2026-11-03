# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node: Optional[TreeNode], minVal: int, maxVal: int):

            if node is None:
                return True

            if node.val <= minVal or node.val >= maxVal:
                return False

            return helper(node.left, minVal, node.val) and helper(node.right, node.val, maxVal)

        return helper(root, -math.inf, math.inf)
