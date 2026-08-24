class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.lru = {}
        self.clock = 0
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.clock += 1
            self.lru[key] = self.clock
            return self.cache[key]

        return -1
        

    def put(self, key: int, value: int) -> None:
        self.clock += 1
        self.lru[key] = self.clock

        if self.size == self.capacity:
            evict = min(list(self.lru.keys()), key=lambda x: self.lru[x])

            del self.cache[evict]
            del self.lru[evict]
            self.size -= 1

        self.cache[key] = value
        self.size += 1

        