class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def _get_hash(self, key) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key, value):
        h = self._get_hash(key)
        self.arr[h] = value

    def get(self, key):
        h = self._get_hash(key)
        return self.arr[h]

t = HashTable()
t.add('march 9', 300)
print(t.get('march 9'))