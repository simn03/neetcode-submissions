# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if root is None:
            return -1
        
        def helper(node: TreeNode, acc: int):

            leftIdx, leftVal = acc, None

            if node.left is not None:
                leftIdx, leftVal = helper(node.left, acc)

            if leftIdx == k:
                return (leftIdx, leftVal)

            currIdx, currVal = leftIdx + 1, node.val

            if currIdx == k:
                return (currIdx, currVal)

            if node.right is None:
                return (currIdx, currVal)
            
            rightIdx, rightVal = helper(node.right, currIdx)

            if rightIdx == k:
                return (rightIdx, rightVal)

            return (rightIdx + 1, node.val)

        (idx, val) = helper(root, 0)

        if val is None:
            return -1

        return val

