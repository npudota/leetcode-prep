class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.HashMap = {}
        

    def get(self, key: int) -> int:
        if key not in self.HashMap:
            return -1
        
    # Save the value, pull it out, and put it back at the end
        value = self.HashMap.pop(key)
        self.HashMap[key] = value
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.HashMap:
            self.HashMap.pop(key)
        elif len(self.HashMap) >= self.capacity:
        # Evict the oldest (first) item
            first_key = next(iter(self.HashMap))
            self.HashMap.pop(first_key)
        self.HashMap[key] = value
