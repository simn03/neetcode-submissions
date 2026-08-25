# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        def debug(node: Optional[ListNode], idx: int = 10):
            if idx == 0 or node is None:
                return ']'
            return(f"{node.val},{debug(node.next, idx - 1)}")

        def printList(node: Optional[ListNode]):
            print(f"[{debug(node, 6)}")
        
        def rec(node: ListNode, idx: int) -> tuple[Optional[ListNode], Optional[ListNode], bool]:

            if node.next is None:
                return (node, None, idx % k == 0)

            head, prevHead, reverse = rec(node.next, idx + 1)

            if idx % k != 0 and not reverse:
                return (node, node, False)

            if idx % k == 0:
                if reverse:
                    node.next.next = prevHead
                if idx != 0:
                    prevHead = head
                    head = node
            else:
                node.next.next = node

            printList(head)

            return (head, prevHead, True)


        head, _, _ = rec(dummy, 0)
        

        return head

