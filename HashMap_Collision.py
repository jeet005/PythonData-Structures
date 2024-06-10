class HashMap:
    def __init__(self):
        self.max = 10
        self.arr = [[] for x in range(0, self.max)]

    def get_hash(self, key):
        h = 0
        for word in key:
            h += ord(word)
        
        return h % self.max
    
    def getItem(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                print(element[1])

    def setItem(self, key, value):
        h = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
            
        if not found:
            self.arr[h].append((key, value))
        
    def delItem(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
        
hh = HashMap()
hh.setItem('march 6', '100')
hh.setItem('march 10', '200')
hh.setItem('march 17', '300')
print(hh.arr)
hh.getItem('march 6')
hh.delItem('march 17')
print(hh.arr)