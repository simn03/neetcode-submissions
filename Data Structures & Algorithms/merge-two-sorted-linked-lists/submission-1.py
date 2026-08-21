# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        curr = head

        next1 = list1
        next2 = list2

        while next1 or next2:

            if next1 is None:
                curr.next = next2
                next2 = None
                break

            if next2 is None:
                curr.next = next1
                next1 = None
                break

            if next1.val < next2.val:
                curr.next = next1
                curr = curr.next
                next1 = next1.next
            else:
                curr.next = next2
                curr = curr.next
                next2 = next2.next


        return head.next


            


        