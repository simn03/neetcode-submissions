# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def helper(self, node: ListNode, idx: int):

        if node.next is None:
            return (node, idx)

        res = self.helper(node.next, idx + 1)

        mid = res[1] / 2

        if idx > mid:
            return (node, res[1])
        
        if mid == idx:
            node.next = None
            return res
        
        tail = res[0]

        temp = node.next
        node.next = tail
        tail = res[0].next
        
        if mid - 0.5 == idx:
            node.next.next = None
        else:
            node.next.next = temp

        return (tail, res[1])

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head is None:
            return None

        self.helper(head, 0)