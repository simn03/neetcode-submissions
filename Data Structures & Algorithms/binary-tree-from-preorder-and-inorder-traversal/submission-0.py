# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        headVal = preorder[0]
        
        head = TreeNode(val=headVal)

        try:
            pivot = inorder.index(headVal)
        except ValueError:
            return self.buildTree(preorder[1:], inorder)

        left = inorder[0:pivot]
        right = inorder[pivot + 1:]

        head.left = self.buildTree(preorder[1:], left)
        head.right = self.buildTree(preorder[1:], right)

        return head
