# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Add l2 to l1
9 9 9
9 9 9 9 9


"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 is None and l2 is None:
            return None

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        l1 = l1 if l1 else ListNode()

        val = v1 + v2

        carry = val // 10
        l1.val = val % 10
        
        if carry > 0:
            l1.next = l1.next if l1.next else ListNode()
            l1.next.val += carry

        l1.next = self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None)

        return l1