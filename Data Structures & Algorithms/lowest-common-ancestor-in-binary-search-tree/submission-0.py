# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def getPath(curr: Optional[TreeNode], target: TreeNode) -> List[TreeNode] | None:

            if curr is None:
                return None

            if curr.val == target.val:
                return [target]

            left = getPath(curr.left, target)

            if left is not None:
                left.append(curr)
                return left

            right = getPath(curr.right, target)

            if right is not None:
                right.append(curr)
                return right

            return None

        pPath = getPath(root, p)
        qPath = getPath(root, q)

        while pPath and qPath:
            if (pPath[0] == qPath[0]):
                return pPath[0]

            if len(pPath) > len(qPath):
                pPath = pPath[1:]
            else:
                qPath = qPath[1:]

        return root

            