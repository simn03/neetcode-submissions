from dataclasses import dataclass
from typing import Optional, Self
import heapq

@dataclass
class Node:
    val: int = 0
    prev: Optional[Self] = None
    valid: bool = True

class MinStack:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.heap = []
        self.len = 0

    def push(self, val: int) -> None:
        node = Node(val=val, prev=self.tail.prev)
        # id(node) acts as a unique tie-breaker to prevent Node comparisons in heap
        heapq.heappush(self.heap, (val, id(node), node))
        self.tail.prev = node
        self.len += 1

    def pop(self) -> None:
        if self.tail.prev is self.head:
            return

        node = self.tail.prev
        node.valid = False  # Mark node as invalid upon removal
        self.tail.prev = node.prev
        self.len -= 1

    def top(self) -> int:
        if self.tail.prev is self.head:
            return 0
        
        return self.tail.prev.val

    def getMin(self) -> int:
        # Lazily pop invalid nodes from top of heap
        while self.heap and not self.heap[0][2].valid:
            heapq.heappop(self.heap)
        
        return self.heap[0][0] if self.heap else 0