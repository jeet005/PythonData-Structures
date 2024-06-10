class HashMap:
    def __init__(self):
        self.max = 100
        self.arr = [None for x in range(0, self.max)]

    def get_hash(self, key):
        h = 0
        for word in key:
            h += ord(word)
        
        return h % self.max
    
    def getItem(self, key):
        h = self.get_hash(key)
        print(self.arr[h])

    def setItem(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def delItem(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        
hh = HashMap()
hh.setItem('Name', 'Sarabjeet')
hh.setItem('Address', 'Street 123')
hh.setItem('phone', '9999999999')
hh.getItem('Name')
hh.delItem('Address')
print(hh.arr)