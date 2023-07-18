class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        
        # Used for key-value matching
        # Save value as value+1, 0 for null checking
        self.dic = OrderedDict()
        self.capa = capacity
        

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value
        
        if len(self.dic) > self.capa:
            self.dic.popitem(last=False)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)