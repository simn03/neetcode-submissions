# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def helper(node: Optional[TreeNode], acc: tuple[int, int]):

            if node is None:
                return acc

            leftIdx, leftVal = helper(node.left, acc)

            if (leftIdx == k):
                return (leftIdx, leftVal)

            currIdx, currVal = leftIdx + 1, node.val

            if (currIdx == k):
                return (currIdx, currVal)

            return helper(node.right, (currIdx, currVal))
            

        (idx, val) = helper(root, (0, -1))

        return val

