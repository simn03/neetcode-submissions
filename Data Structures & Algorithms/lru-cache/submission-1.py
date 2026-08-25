from dataclasses import dataclass

@dataclass
class Node:
    key: int
    val: int
    next: Optional['Node'] = None
    prev: Optional['Node'] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node):
        prevN = node.prev
        nextN = node.next

        assert(prevN and nextN)

        prevN.next = nextN
        nextN.prev = prevN

        node.next = None
        node.prev = None

    def insert(self, node: Node):
        temp = self.head.next

        assert(temp)

        self.head.next = node
        node.prev = self.head

        temp.prev = node
        node.next = temp
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if (len(self.cache) >= self.capacity):
            node = self.tail.prev
            assert(node)

            self.remove(node)
            del self.cache[node.key]

        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node


        