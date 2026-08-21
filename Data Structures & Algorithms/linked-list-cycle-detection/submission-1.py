# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def helper(self, head1, head2):
        if head1 is None or head2 is None:
            return False

        if head1 == head2:
            return True

        if head2.next is None:
            return False

        return self.helper(head1.next, head2.next.next)

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False
        
        return self.helper(head, head.next)