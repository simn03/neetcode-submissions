# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def rec(self, root: Optional[ListNode], curr: Optional[ListNode]):

        if curr is None:
            return root

        root = self.rec(root, curr.next)

        if root == None:
            return None

        if root == curr or root.next == curr:
            curr.next = None
            return None

        temp = root.next
        root.next = curr
        curr.next = temp

        return temp

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head is None:
            return None

        self.rec(head, head.next)