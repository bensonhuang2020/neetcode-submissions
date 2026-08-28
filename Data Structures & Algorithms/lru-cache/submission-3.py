class LRUCache:

    def __init__(self, capacity: int):
        # ordered dict keeps things the order you put them in
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # getting means you should move it to the end
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # if you can get it, move it to the end, either way, replace the value
        if self.cache.get(key):
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        # if at capacity, just remove the first item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
