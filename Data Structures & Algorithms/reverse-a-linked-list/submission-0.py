# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, node: ListNode):
        
        if node.next is None:
            return (node, node)

        new = self.reverse(node.next)

        new[0].next = node
        node.next = None

        return (node, new[1])


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None;
        
        return self.reverse(head)[1]