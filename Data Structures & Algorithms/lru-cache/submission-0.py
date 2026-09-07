class Node:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        return node.val
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        node = Node(key, value)
        self.cache[key] = node
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        if len(self.cache) > self.capacity:
            lru = self.left.next
            lru.prev.next = lru.next
            lru.next.prev = lru.prev
            del self.cache[lru.key]