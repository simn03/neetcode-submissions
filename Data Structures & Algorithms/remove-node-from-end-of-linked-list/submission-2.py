# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Focus on a recursive solution. Go through to the end of the list until the node is NULL.
Once this occurs, return 0 as the base case and begin incrementing the returned value as we pop the call stack. 

Example:
At the 1st element from the end, the returned value will be 0 (returned from the base case).
At the 2nd element from the end, the returned value will be 1 (incremented from previous return value)

For the kth element from the end, the returned value will be k - 1

Using this induction, we can assume that once we reach the n + 1th element from the end, 
we will have a returned value of n. This would mean the very next element in the list is the element to remove.

This allows us to simply remove that node via simple pointer manipulation:
    Set the current node's NEXT to the target node's NEXT

Finally, there is the case of the target node being removed as the very first in the list.
This would mean we could not use the pointer manipulation to update the current node to skip the target node. In this case, we simply check to see if the returned final index is equal to the target node and then increment the head of the list to return the second item as the new head.
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return None

        def rec(node: Optional[ListNode]):
            if node is None:
                return 0

            idx = rec(node.next)

            if idx == n:
                new = node.next.next
                node.next = new

            return idx + 1

        popped = rec(head)

        if popped == n:
            head = head.next

        return head