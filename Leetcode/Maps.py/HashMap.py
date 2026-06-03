
class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketsize = 10
        self.bucket = [None for i in range(self.bucketsize)]
        self.count = 0

    def size(self):
        return self.count
    
    def getBucketIndex(self, hc):
        return abs(hc)%(self.bucketsize)
    
    def insert(self, key, value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        # print(index)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return 
            head = head.next
        head = self.bucket[index]
        newNode = MapNode(key,value)
        newNode.next = head
        self.bucket[index] = newNode
        self.count += 1

    def getValue(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
    
    def remove(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.bucket[index] = head.next
                else:
                    prev = head.next
                self.count -= 1
                return head.next
            prev = head
            head = head.next
        return None



m = Map()
m.insert("Abhinav",2)
m.insert("Kartavya",9)
print(m.size())
m.remove("Abhinav")
print(m.size())