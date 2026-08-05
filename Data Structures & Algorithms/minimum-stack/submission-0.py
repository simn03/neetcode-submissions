from dataclasses import dataclass
from typing import Self, Optional
import heapq

@dataclass
class Node:
    val: int = 0
    prev: Optional[Self] = None
    idx: int = -1

class MinStack:

    head: Node
    tail: Node
    len: int = 0

    heap = []
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.tail.prev = self.head

    def push(self, val: int) -> None:
        node = Node(val=val, prev=self.tail.prev, idx=self.len)

        heapq.heappush(self.heap, (val, self.len))

        self.tail.prev = node
        self.len += 1

    def pop(self) -> None:
        if self.tail.prev is None:
            return

        node = self.tail.prev
        self.tail.prev = node.prev

        del node

        self.len -= 1

    def top(self) -> int:
        if self.tail.prev is None:
            return 0
        
        return self.tail.prev.val


    def getMin(self) -> int:
        while self.heap[0][1] >= self.len:
            heapq.heappop(self.heap)
        return self.heap[0][0]
