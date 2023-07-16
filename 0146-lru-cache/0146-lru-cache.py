class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}

        # left -> LRU -> ... -> MRU -> right !!!!!
        self.left = Node()
        self.right = Node()
        self.left.next, self.right.prev = self.right, self.left

    # remove from doubly linked list (keep in hashmap)
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # insert into MRU position
    def insertMRU(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.remove(self.nodes[key])
            self.insertMRU(self.nodes[key])
            return self.nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])
        self.nodes[key] = Node(key, value)
        self.insertMRU(self.nodes[key])

        if len(self.nodes) > self.capacity:
            lru = self.left.next # !!!!!
            self.remove(lru)
            del self.nodes[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)