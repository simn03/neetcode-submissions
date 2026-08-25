import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Initial Idea:

Use a heap to store the minimum value at each iteration.
Each item of the heap stores the index of the list (referencing the head node)

Use an initial pass to place all inner list heads into the heap.

Pop the min value to place next in the list. Push the next item in the popped inner list into
the heap.

Run Time:
    Initial Pass: O(k*logk) -> Pass over all (k) lists and push the values into the heap (logk)
    Remaining Lists: O(N*logk) -> Pass over all element (N) and push the values into the heap (logk)
    Total: O(N*logk)
"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        pq = []

        for i, node in enumerate(lists):
            if node is None:
                continue
            
            heapq.heappush(pq, (node.val, i, node))

        head = ListNode(-1, None)

        curr = head

        while pq:
            popped = heapq.heappop(pq)
            node = popped[2]
            curr.next = node
            curr = node

            if node.next:
                heapq.heappush(pq, (node.next.val, popped[1], node.next))

        curr.next = None

        return head.next

        

