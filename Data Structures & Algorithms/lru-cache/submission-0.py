class Node:
    def __init__(self, val, key):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node):
        prevMRU = self.head.next
        self.head.next = node
        node.prev, node.next = self.head, prevMRU
        prevMRU.prev = node 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            LRU = self.tail.prev
            self.remove(LRU)
            del self.cache[LRU.key]

        newNode = Node(value, key)
        self.insert(newNode)
        self.cache[key] = newNode


        
