# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return None

        def rec(node: Optional[ListNode]):
            if node is None:
                return 0

            idx = rec(node.next)

            if idx == n:
                new = node.next.next if node.next else None
                node.next = new

            return idx + 1

        popped = rec(head)

        if popped == n:
            head = head.next

        return head