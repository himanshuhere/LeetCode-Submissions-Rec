class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        
        #initial DLL cofiguration
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        
        elif len(self.dic) == self.capacity:
            self._remove(self.tail.prev)
            
        n = Node(key, value)
        self._add(n)

    def _remove(self, node):
        del self.dic[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        self.dic[node.key] = node
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head