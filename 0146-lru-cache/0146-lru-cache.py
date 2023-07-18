class LRUCache:

    def __init__(self, capacity: int):
        from collections import defaultdict
        
        # Used for key-value matching
        # Save value as value+1, 0 for null checking
        self.dic = defaultdict(int) 
        self.dll = [[None, None] for _ in range(10005)]
        self.head = None
        self.tail = None
        self.capa = capacity
        self.num = 0
        

    def get(self, key: int) -> int:
        if self.dic[key]:
            self.update(key)
        return self.dic[key] - 1
            

    def put(self, key: int, value: int) -> None:
        if self.dic[key]: # existing key
            self.update(key=key)
        elif self.head == None: # first put
            self.num += 1
            self.head, self.tail = key, key
        else: # new key
            self.num += 1
            self.to_head(key)
            
            if self.num > self.capa: # evict
                self.dic[self.tail] = 0
                self.tail = self.dll[self.tail][0]
                self.dll[self.tail][1] = None              

        self.dic[key] = value + 1
    
    
    def update(self, key):
        if key == self.head:
            return
        elif key == self.tail:
            self.tail = self.dll[key][0]
            self.dll[self.tail][1] = None
            self.to_head(key)
        else:
            k_head, k_tail = self.dll[key][0], self.dll[key][1]
            # if k_tail:
            self.dll[k_tail][0] = k_head
            # if k_head:
            self.dll[k_head][1] = k_tail                
            self.to_head(key)
        
        
    def to_head(self, key):
        self.dll[self.head][0] = key
        self.dll[key] = [None, self.head]
        self.head = key
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)