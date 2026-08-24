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

Use 2 passes. The first goes over the main list. Each cloned node is kept in a map storing
the original to the copy. The random value then checks this map for an existing node to use. If this node does not exist, it creates it and places it in the map instead.
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        cloned: dict[Node, Node] = {}

        def rec(node: Optional[Node]):
            if node is None:
                return None

            newNode = None

            if node in cloned:
                newNode = cloned[node]
            else:
                newNode = Node(node.val)
                cloned[node] = newNode

            if newNode.next is None:
                newNode.next = cloned[node.next] if node.next in cloned else rec(node.next)

            if newNode.random is None:
                newNode.random = cloned[node.random] if node.random in cloned else rec(node.random)

            return newNode

        return rec(head)

