class Hashtable:
    def __init__(self, size=8):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def __len__(self):
        return sum(len(bucket) for bucket in self.table)
        
    def _hash(self, key):
        return hash(key) % self.size
        
    def add(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])
        
    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(f"Key '{key}' not found")
        
    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found")
        
    def get_size(self):
        return self.size
        
    def is_empty(self):
        return len(self) == 0
if __name__ == '__main:__':
    data = ['goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', 'cow', 'cat']
    # make a hash table with key-value pairs: 'goat': 0, 'pig': 1, 'chicken': 2, etc. 
    h = Hashtable()
    for i in range(len(data)):
        h.add(data[i], i)       # the key is data[i], the value is i

    # print the hash table items
    for key in data:
        print(h.get(key))
    
    # test the method get() and if items in the hash table are correct
    for i in range(len(data)): 
        assert h.get(data[i]) == i 

    # test the method get_size()
    n = h.get_size() # it depends on the default value of your hash table
    assert n == 8 
    assert len(h) == 8 # it depends on the number of items in the hash table

    # test the method remove() and is_empty()
    for i in data: 
        h.remove(i) 
    print(h.is_empty()) 
    assert h.is_empty()
    assert len(h) == 0