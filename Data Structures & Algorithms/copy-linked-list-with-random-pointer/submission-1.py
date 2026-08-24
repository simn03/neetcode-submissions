"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Initial Idea:

Recursively rebuild the the list while maintaining a map of the newly created nodes.

Base Case:
    If the node is None, return None

Generic Case:
    Each node first checks to see if it already exists in the cloned map. If yes, return that saved node.
    If not, continue to creating the node. For each node property (next, random), first check to see if
    that node already exists in the cache. If yes, return the cached value for that property. Otherwise,
    recursively clone the missing node.
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        cloned: dict['Node', 'Node'] = {}

        def rec(node: 'Optional[Node]') -> 'Optional[Node]':
            if node is None:
                return None

            if node in cloned:
                return  cloned[node]

            newNode = Node(node.val)
            cloned[node] = newNode

            newNode.next = cloned[node.next] if node.next in cloned else rec(node.next)

            newNode.random = cloned[node.random] if node.random in cloned else rec(node.random)

            return newNode

        return rec(head)

