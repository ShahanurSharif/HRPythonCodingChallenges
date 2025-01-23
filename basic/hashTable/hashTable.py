class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def _get_hash(self, key) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self._get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self._get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self._get_hash(key)
        self.arr[h] = None

t = HashTable()
t['march 9'] =300
t['march 6'] =301
del t['march 6']
print(t.arr)