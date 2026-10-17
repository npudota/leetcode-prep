class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.cap = capacity
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        nxt = self.right
        prev = self.right.prev
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        self.mp[key] = Node(key,value)
        self.insert(self.mp[key])

        if len(self.mp) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.mp[lru.key]

    

    
   
        
